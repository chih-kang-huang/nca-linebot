from __future__ import unicode_literals
import os
from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
# import pandas as pd

import random
import order_lib
import order
import help

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
# admins = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=admins")['idLINE'].to_list()
admins = [
    'Uefa7580b75912cf5cbd1be6dba8dafbe', # 洪仲杰
    # 'U75851bf4cd33d189464170b50df30ee8', # 陳宜祥
    #'U45eac4b2d3598d5bb9ee33cee0518d45', # 蕭崇聖
    #'U3ff60662d9e6b90835aa52fa8cfb6ef5', # 賴冠鏵
    #'U0772fe2a09529c65b7a7c0163a92feda', # 林俊宇
    #'Ua96931bfef5d06d91250f883559a0750', # 陳怡誠
    #'U0689f87646c44772528af8b2b4405117', # 洪梓彧
    #'Ue8f9f131ad9ce7a424ec19b1fd82b076', # 張晉源
    'Uad0875dc50aa4eb10c573534b9b1e1ac', # 鄭承祐
    'U8ff33cad30112b82f195d530f98dcabb', # 黃治綱
    'Ufa1ac5a64269db78b5334e794b2fd942', # STL
    'Ucb43705a1d091f13a356938a0cc04cee', # 鄭承祐
    'U90973a2215664f879f8e650b0f59fdd4', # 白泉祐
    'Ub64433aecd75d919542e90cb217ef476', # 于恆生
    'Ucb47e88904a75859327afb509d7c3db3', # 袁子晉
]
# groups = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=groups")['idLINE'].to_list()
groups = [
    'Cf4a08527ed49eab9d2cf53a8b0309cf0', # 午餐群組
    'Ce6071d5887fd879bc620143fce3c8382', # 測試群組
    'C49243ad433dd8bd975340c6a83207c84', # group id test
    'Ca9396f3333d4933d121e3d060959b5a0', # group id test 2
    'Cdef1757ed89b5f441e4496932a0baaa0', # 午餐群組
]
# restaurants = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=restaurants")['name'].to_list()
restaurants = [
    '大盛', '六星', '日日佳', '甲一', '皇上皇',
    '華圓', '寶多福', '小林', '月枱', '呂媽媽',
    '佳臻', '小煮角', '中一排骨', '田園小轆', '能量小姐',
    '開心越南', '兄弟', '榮興', '簡單', '好味', '華園',
    '全樂', '高又鮮', '簡單夏',
]
# beverages = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=beverages")['name'].to_list()
beverages = [
    '可不可', '得正', '烏弄',
]


# 網域名稱、機器人使用說明
# domain_name = 'https://' + app_name + '.herokuapp.com/' # heroku
domain_name = 'https://' + app_name + '.fly.dev/' # fly.io
description = '指令輸入格式：[指令]/[內容1]/[內容2]...\n\
餐廳範例： 點/13/5/3/2\n\
飲料範例： 喝/3,L,無糖少冰/12,M,全糖/6,中杯,半糖多冰\n\
指令：說明、吃、點、取消、統計、截止、清除'
# 指令：說明、吃、點、取消、統計、截止、清除\n\
# 詳見 https://github.com/CheesyPicodon/ncu-line-bot'

# variables
current_restaurant = ""
current_beverage = ""

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

@app.route('/detail_drink')
def showDetailDrink():
    return render_template('detail_drink.html')

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
    if '/' not in message or group_id not in groups:
    #if '/' not in message:
        return
    message = message.replace(' ','').replace('\n','').split('/',1)
    print(message)

    # command's format: [command, parameters]
    command = message[0]
    parameters = message[1]
    reply = ''
    keyboard=''

    # 使用說明
    if command == '說明':
        reply = description
#        line_bot_api.reply_message(event.reply_token, help.createWithFlex())


    # 列出可提供菜單的餐廳
    elif command == '餐廳':
        for restaurant in restaurants:
            reply += ( restaurant + '\n' )

    # 列出可提供菜單的飲料
    elif command == '飲料':
        for beverage in beverages:
            reply += ( beverage+ '\n' )

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
#            reply = order_lib.printMenu(restaurant)
#            keyboard = '1'
#            keyboard = order_lib.printMenu(restaurant)
            line_bot_api.reply_message(
                event.reply_token,
#                [
#                    TextSendMessage(keyboard),
                    help.createWithFlex(restaurant)
#                ]
            )
            #order.createOrderForm(restaurant)
            #reply = order.getMenu(restaurant)
        else:
            reply = '查無此餐廳'

    elif command == '訂' and user_id in admins:
        beverage = parameters
        if beverage in beverages:
            order_lib.setBeverage(beverage)
            reply = order_lib.printDrink(beverage)
        else:
            reply = '查無此飲料店'

    # 清除訂餐資料
    # 需要admin權限
    elif command == '清除' and user_id in admins:
        order_lib.clear()
        reply = '清除資料'

    # 已經決定好餐廳才能使用的指令
    if order_lib.getRestaurant() or order_lib.getBeverage() :

        # 點餐
        if command == '點':
            reply = order_lib.addOrder(user_id, parameters)
            # reply = order.addOrder(user_id, parameters)

        # 點飲料
        if command == '喝':
            reply = order_lib.addOrderDrink(user_id, parameters)

        # 取消點餐
        elif command == '取消':
            reply = order_lib.cancelOrder(user_id, parameters)

#       # 取消飲料
        elif command == '飲取消':
            reply = order_lib.cancelOrderDrink(user_id, parameters)

        # 統計餐點並顯示明細表(網頁)
        elif command == '統計' and user_id in admins:
            orders = order_lib.getOrder()
            restaurant = order_lib.getRestaurant()
            menu = order_lib.getMenu(restaurant)
            foods = order_lib.countOrder(orders)
            reply = order_lib.printStatistic(foods, menu)
            reply += ('\n' + order_lib.showDetailAsHtml(line_bot_api, orders, menu, domain_name))


        # 統計飲料並顯示明細表(網頁)
        elif command == '飲統計':
#            foods = order_lib.countOrder(orders)
#            reply = order_lib.printStatistic(foods, menu)
            orders = order_lib.getOrderDrink()
            beverage = order_lib.getBeverage()
            menu = order_lib.getDrink(beverage)
            reply += ('\n' + order_lib.showDetailDrinkAsHtml(line_bot_api, orders, menu, domain_name))

        # 回覆明細表
        elif command == '明細':
            orders = order_lib.getOrder()
            restaurant = order_lib.getRestaurant()
            menu = order_lib.getMenu(restaurant)
            reply = order_lib.printDetail(line_bot_api, orders, menu)
            reply += ('\n' + order_lib.showDetailAsHtml(line_bot_api, orders, menu, domain_name))

        # 回覆明細表(飲)
        elif command == '飲明細':
            orders = order_lib.getOrderDrink()
            beverage = order_lib.getBeverage()
            menu = order_lib.getDrink(beverage)
            reply = order_lib.printDetailDrink(line_bot_api, orders, menu)
            reply += ('\n' + order_lib.showDetailDrinkAsHtml(line_bot_api, orders, menu, domain_name))

        # 關閉點餐
        # 需要admin權限
        elif command == '截止' and user_id in admins:
            order_lib.setRestaurant('')
            order_lib.setBeverage('')

    # 回覆訊息
    if reply:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(reply))

# main func
if __name__ == '__main__':
    # local test
    # order_lib.addOrderDrink("ck","喝/1,L,haha")
    app.run()
