# -*- coding: utf-8 -*-
"""
Created on Sat Nov 5 2022

@author: colleabois
"""
import os
import pandas as pd
from datetime import date

restaurant_folder = 'data/restaurant/'
data_path = 'data/data.json'
order_path = 'data/order.csv'
detail_path = 'static/detail.txt'
sheet_id = os.environ.get('SHEET_ID')

def getStoreId(name):
    """ Find an the ID of the store from Google Sheet
    This function can be ignored if we can read onglets with chinese name 
    :param name<string>: the name of the store
    """
    # Call list of stores
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=stores")
    # Return the first Id that matches the name
    for i in range(len(df.index)):
        if df.iat[i,1]==name:
            return df.iat[i,0]
    return "Store Id not found."

def getMenu(name):
    """ 
    :param name<string>: the name of the store
    """
    # If read from local folder
    # df = pd.read_csv(restaurant_folder + name + '.csv', encoding = 'utf-8')
    store_id = getStoreId(name)
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={store_id}")
    assert(df.columns.to_list()[0]==name)
    # Show only result of second and third column
    menu = pd.DataFrame(df.iloc[:, 1:3]).to_string()
    return menu

def createOrderForm(name):
    """ 
    Create a dedicated order form for a store and save it to order folder.
    :param name<string>: the name of the store
    """
    # If read from local folder
    # df = pd.read_csv(restaurant_folder + name + '.csv', encoding = 'utf-8')
    store_id = getStoreId(name)
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={store_id}")
    elements = df.columns.to_list()
    assert(elements[0]==name)
    elements[0] = "userId"
    order = pd.DataFrame(columns=elements)
    order.to_csv("data/order/order_"+name+"_"+date.today().strftime("%b-%d-%Y")+".csv",\
        index=False)
    return order

def addOrder(user_id, orders, current_beverage, current_restaurant):
    # Set store name
    store_name = ""
    orders = orders.split('/')
    if orders[0] == "點":
        store_name = current_restaurant
    elif orders[0] == "喝":
        store_name = current_beverage

    # Read data
    path_data = "data/order/order_"+store_name+"_"+date.today().strftime("%b-%d-%Y")+".csv"
    df = pd.read_csv(path_data)
  
    for order in orders[1:]:
        order = order.split(',')
        # Fill with blank space if not specified
        new_row = [user_id]+order+["" for k in range(len(df.columns)-len(order)-1)]
        # Add new row to the end of dataframe
        df.loc[len(df)] = new_row

    # Save data
    df.to_csv(path_data,index=False)

    return '收到'

def getOrder(current_restaurant,current_beverage):
    """ 
    Concatenate current restaurant and current beverage order.
    Return the order table as a string. 
    """
    # Read data
    path_data_rest = "data/order/order_"+current_restaurant+"_"+date.today().strftime("%b-%d-%Y")+".csv"
    df1 = pd.read_csv(path_data_rest).to_string()
    path_data_bev = "data/order/order_"+current_beverage+"_"+date.today().strftime("%b-%d-%Y")+".csv"
    df2 = pd.read_csv(path_data_bev).to_string()
    return "點/" + current_restaurant + "\n" + df1 +\
             "\n喝/"+ current_beverage  + "\n" + df2

def cancelOrder(user_id, cancel_orders, current_restaurant):
    path_data = "data/order/order_"+current_restaurant+"_"+date.today().strftime("%b-%d-%Y")+".csv"
    df = pd.read_csv(path_data)
        
    if cancel_orders:
        cancel_orders = cancel_orders.split('/')
        new_df = df.drop(index=[int(s) for s in cancel_orders])
    else: # Cancel all order if the user didn´t give specification
        new_df = df.loc(df["userId"]!=user_id)
    
    # Save data
    new_df.to_csv(path_data,index=False)

    return '取消訂單'
