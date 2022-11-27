# -*- coding: utf-8 -*-
"""
Created on Sat Nov 5 2022

@author: colleabois & cheesypicodon
"""

import json
import csv
import os
from datetime import date
# import pandas as pd

restaurant_folder = 'data/restaurant/'
beverage_folder= 'data/beverage/'
data_path = 'data/data.json'
order_path = 'data/order.csv'
drink_order_path = 'data/drink_order.csv'
detail_path = 'static/detail.txt'
drink_detail_path = 'static/drink_detail.txt'
# detail_url = 'https://ncu-line-bot.fly.dev/detail'

# return data in data.json
def getData():
    with open(data_path, 'r', encoding = 'utf-8') as jsonFile:
        data = json.load(jsonFile)
    return data

# edit data in data.json
def setData(data):
    with open(data_path, 'w', encoding = 'utf-8') as jsonFile:
        json.dump(data, jsonFile)

# return today's restaurant
def getRestaurant():
    data = getData()
    return data['restaurant']

# set today's restaurant
def setRestaurant(restaurant):
    data = getData()
    data['restaurant'] = restaurant
    setData(data)

# get a restaurant's menu
def getMenu(restaurant):
    with open(restaurant_folder + restaurant + '.csv', newline = '', encoding = 'utf-8') as menuFile:
        menu = list(csv.reader(menuFile))
        return menu

# return today's beverage
def getBeverage():
    data = getData()
    return data['beverage']

# set today's beverage
def setBeverage(beverage):
    data = getData()
    data['beverage'] = beverage
    setData(data)

# get a beverage's menu
def getDrink(beverage):
    with open(beverage_folder + beverage + '.csv', newline = '', encoding = 'utf-8') as menuFile:
        menu = list(csv.reader(menuFile))
        return menu

# print a restaurant's menu
def printMenu(restaurant):
    reply = ''
    menu = getMenu(restaurant)
    for food in menu:
        # no. / name / price
        reply += ( food[0] + '. ' + food[1] + ' ' + food[2] + '\n' )
    return reply


## print a beverage's menu
def printDrink(beverage):
    reply = ''
    menu = getDrink(beverage)
    for drink in menu:
        # no. / name / price 1 / price 2 ...etc
        reply += ( drink[0] + '. ' + drink[1] + ' ' + drink[2] + ' ' + drink[3] + '\n' )
    return reply

# check if user's input is valid
def checkValidity(order):
    menu = getMenu(getRestaurant())
    if order.isnumeric():
        if int(order) > 0 and int(order) < len(menu):
            return True
    return False

# add order(s) into order.csv
def addOrder(user_id, orders):
    orders = orders.split('/')
    with open(order_path, 'a+', encoding = 'utf-8') as orderFile:
        for order in orders:
            # validate parameter
            if order.isnumeric():
                orderFile.write(user_id + ',' + order + '\n')
            else:
                return '請依照格式輸入'
    return '收到'


def addOrderDrink(user_id, orders):
    orders = orders.split('/')
    with open(drink_order_path, 'a+', encoding = 'utf-8') as orderFile:
        for order in orders:
            order = order.split(',')
            # validate parameter
            if len(order) == 3 and order[0].isnumeric():
                orderFile.write(user_id + ',' + order[0] + ',' + order[1] + ',' + order[2] + '\n')
            else:
                return '請依照格式輸入'
    return '收到'

# cancel and remove order(s) from order.csv
def cancelOrder(user_id, cancel_orders):
    orders = getOrder()
    os.remove(order_path)
    # if user does input parameters, cancel particular orders
    if cancel_orders:
        cancel_orders = cancel_orders.split('/')
        for order in orders:
            if order[0] != user_id:
                addOrder(order[0], order[1])
            elif order[1] not in cancel_orders:
                addOrder(order[0], order[1])
    # if user does not input parameters, cancel all the orders that match user_id
    else:
        for order in orders:
            if order[0] != user_id:
                addOrder(order[0], order[1])
    return '取消訂單'


#def cancelOrderDrink(user_id, cancel_orders):
#    orders = getOrderDrink()
#    os.remove(drink_order_path)
#    # if user does input parameters, cancel particular orders
#    if cancel_orders:
#        cancel_orders = cancel_orders.split('/')
#        for order in orders:
#            if order[0] != user_id:
#                addOrderDrink(order[0], order[1], order[2], order[3])
#            elif order[1] not in cancel_orders:
#                addOrder(order[0], order[1])
#    # if user does not input parameters, cancel all the orders that match user_id
#    else:
#        for order in orders:
#            if order[0] != user_id:
#                addOrder(order[0], order[1])
#    return '取消飲料'

# return orders
def getOrder():
    with open(order_path, newline = '', encoding = 'utf-8') as orderFile:
        orders = list(csv.reader(orderFile))
    return orders

def getOrderDrink():
    with open(drink_order_path, newline = '', encoding = 'utf-8') as orderFile:
        orders = list(csv.reader(orderFile))
    return orders

# count number of each items via dict
def countOrder(orders):
    foods = {}
    for order in orders:
        foods[order[1]] = foods[order[1]] + 1 if order[1] in foods else 1
    return foods

# print each items' number, total number, and price
def printStatistic(foods, menu):
    reply = ''
    total = 0
    total_price = 0
    for food in foods:
        try:
            food_name = menu[int(food)][1]
            food_price = menu[int(food)][2]
            reply += ( food_name + ' ' + str(foods[food]) + '份\n')
            total += foods[food]
            total_price += ( int(food_price) * foods[food] )
        except:
            reply += '查無資料\n'
    reply += ( '共' + str(total) + '份' + str(total_price) + '元' )
    return reply

# write orders into detail.txt which is loaded by detail.html and show to the users
def showDetailAsHtml(line_bot_api, orders, menu, domain_name):
    if os.path.isfile(detail_path):
        os.remove(detail_path)
    order_no = 1
    for order in orders:
        try:
            user_name = line_bot_api.get_profile(order[0]).display_name
        except:
            user_name = order[0]
        food_name = menu[int(order[1])][1]
        food_price = menu[int(order[1])][2]
        with open(detail_path, 'a+', encoding = 'utf-8') as detailFile:
            detailFile.write( str(order_no) + '. ' + user_name + ' / ' + food_name + ' / ' + food_price + '元\n' )
        order_no += 1
    return domain_name + 'detail'

def showDetailDrinkAsHtml(line_bot_api, orders, menu, domain_name):
    if os.path.isfile(drink_detail_path):
        os.remove(drink_detail_path)
    order_no = 1
    for order in orders:
        try:
            user_name = line_bot_api.get_profile(order[0]).display_name
        except:
            user_name = order[0]
        food_name = menu[int(order[1])][1] 
        food_size = str(order[2])
        food_comment = str(order[3])
        if food_size in ['M',' M','M ','中杯','中','m',' m','m ']:
            if menu[int(order[1])][2] in ['', ' '] :
                food_price = 100000
            else:
                food_price = menu[int(order[1])][2]
        else:
            if menu[int(order[1])][3] in ['', ' '] :
                food_price = 100000
            else:
                food_price = menu[int(order[1])][3]
        with open(drink_detail_path, 'a+', encoding = 'utf-8') as detailFile:
            detailFile.write( str(order_no) + '. ' + user_name + ' / ' + food_name + ' (' + food_size + ') ' + food_comment + ' / ' + food_price + '元\n' )
        order_no += 1
    return domain_name + 'detail_drink'

# print orders via line bot
def printDetail(line_bot_api, orders, menu):
    order_no = 1
    reply = ''
    total_price = 0
    for order in orders:
        try:
            user_name = line_bot_api.get_profile(order[0]).display_name
        except:
            user_name = order[0]
        food_name = menu[int(order[1])][1]
        food_price = menu[int(order[1])][2]
        reply += ( str(order_no) + '. ' + user_name + '/' + food_name + '/' + food_price + '元\n' )
        order_no += 1
        total_price += int(food_price)
    reply += ('便當共' + str(total_price) +'元')
    return reply

def printDetailDrink(line_bot_api, orders, menu):
    order_no = 1
    reply = ''
    total_price = 0
    for order in orders:
        try:
            user_name = line_bot_api.get_profile(order[0]).display_name
        except:
            user_name = order[0]
        food_name = menu[int(order[1])][1] 
        food_size = str(order[2])
        food_comment = str(order[3])
        if food_size in ['M',' M','M ','中杯','中','m',' m','m ']:
            if menu[int(order[1])][2] in ['', ' '] :
                food_price = str('100000')
            else:
                food_price = str(menu[int(order[1])][2])
        else:
            if menu[int(order[1])][3] in ['', ' '] :
                food_price = str('100000')
            else:
                food_price = str(menu[int(order[1])][3])
        reply += ( str(order_no) + '. ' + user_name + '/' + food_name + ' (' + food_size +')' +  ' ' + food_comment + '/' + food_price + '元\n' )
        order_no += 1
        total_price += int(food_price)
    reply += ('飲料共' + str(total_price) +'元')
    return reply

# remove unnecessary files
def clear():
    if os.path.isfile(drink_order_path):
        os.remove(drink_order_path)
    if os.path.isfile(order_path):
        os.remove(order_path)
    if os.path.isfile(detail_path):
        os.remove(detail_path)
