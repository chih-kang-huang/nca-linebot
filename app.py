from __future__ import unicode_literals
import os
from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import pandas as pd

import random
import order_lib

app = Flask(__name__)

# get KEYS from your environment variable
channel_secret = os.environ.get('LINE_CHANNEL_SECRET')
channel_access_token = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
app_name = 'ncu-line-bot'

#https://docs.google.com/spreadsheets/d/1OZaZYPPFPVo5EuThuyjS3STR8nMf7peSjK673_bPDHE/gviz/tq?tqx=out:csv&sheet=中一排骨

# 管理員、可用群組、餐廳名單
sheet_id = os.environ.get('SHEET_ID')
admins = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=admins")['idLINE'].to_list()
groups = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=groups")['idLINE'].to_list()
restaurants = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=restaurants")['name'].to_list()

# 網域名稱、機器人使用說明
domain_name = 'https://' + app_name + '.herokuapp.com/'
description = '指令輸入格式：[指令]/[內容1]/[內容2]...\n\
指令：說明、吃、點、取消、統計、截止、清除\n\
詳見 https://github.com/CheesyPicodon/ncu-line-bot'

# root
@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# Webhook callback endpoint
@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret.')
        abort(400)
    return 'OK'

# return 明細表
@app.route('/detail')
def showDetail():
    return render_template('detail.html')


### 主程式

# decorator 判斷 event 為 MessageEvent
# event.message 為 TextMessage
# 所以此為處理 TextMessage 的 handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    print(event)

    # get user id, group id and message
    message = event.message.text
    message_type = event.source.type
    user_id = event.source.user_id
    group_id = event.source.group_id if message_type == 'group' else ''

    # handle command and process string
    # 字串需要包含'/'以及在指定群組才做處理
    #if '/' not in message or group_id not in groups:
    if '/' not in message:
        return
    message = message.replace(' ','').replace('\n','').split('/',1)
    print(message)

    # command's format: [command, parameters]
    command = message[0]
    parameters = message[1]
    reply = ''

    # 使用說明
    if command == '說明':
        reply = description

    # 列出可提供菜單的餐廳
    elif command == '餐廳':
        for restaurant in restaurants:
            reply += ( restaurant + '\n' )

    # 隨機選餐廳
    elif command == '抽籤':
        random_index = random.randint(1,len(restaurants))-1
        reply = '抽籤結果是...\n\n' + restaurants[random_index] + '！'

    # 決定要吃的餐廳
    # 需要admin權限
    elif command == '吃' and user_id in admins:
        restaurant = parameters
        if restaurant in restaurants:
            order_lib.setRestaurant(restaurant)
            reply = order_lib.printMenu(restaurant)
        else:
            reply = '查無此餐廳'

    # 清除訂餐資料
    # 需要admin權限
    elif command == '清除' and user_id in admins:
        order_lib.clear()
        reply = '清除資料'

    # 已經決定好餐廳才能使用的指令
    if order_lib.getRestaurant():

        # 點餐
        if command == '點':
            reply = order_lib.addOrder(user_id, parameters)

        # 取消點餐
        elif command == '取消':
            reply = order_lib.cancelOrder(user_id, parameters)

        # 統計餐點並顯示明細表(網頁)
        elif command == '統計':
            orders = order_lib.getOrder()
            restaurant = order_lib.getRestaurant()
            menu = order_lib.getMenu(restaurant)
            foods = order_lib.countOrder(orders)
            reply = order_lib.printStatistic(foods, menu)
#            reply += ('\n' + order_lib.showDetailAsHtml(line_bot_api, orders, menu, domain_name))

        # 回覆明細表
        elif command == '明細':
            orders = order_lib.getOrder()
            restaurant = order_lib.getRestaurant()
            menu = order_lib.getMenu(restaurant)
            reply = order_lib.printDetail(line_bot_api, orders, menu)

        # 關閉點餐
        # 需要admin權限
        elif command == '截止' and user_id in admins:
            order_lib.setRestaurant('')

    # 回覆訊息
    if reply:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(reply))

# main func
if __name__ == '__main__':
    app.run()