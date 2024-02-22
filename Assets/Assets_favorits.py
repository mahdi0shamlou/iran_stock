import yfinance as yf
from mysql.connector import connect, Error
import mysql.connector
def Get_historical_data_of_symbols_from_yfinance(symbol_list, day_ago=30):
    history_list = []
    for i in symbol_list:
        symbols = yf.Ticker(i[0])
        data = symbols.history(period='100d')
        #print(len(data))
        #print(data["Close"])
        #print(len(data['Close'][(len(data)-1)-day_ago:len(data)-1]))
        history_list.append([i[0], i[1], data['Close'][(len(data)-1)-day_ago:len(data)-1], i[2]])
    return history_list
def Get_profit_of_list(symbol_list, day_ago):
    countr = 0
    day_ago = day_ago - 1
    for i in symbol_list:
        countr = i[3]
        i.pop()
        profit_buy = i[2][day_ago] - i[2][0]
        profit_sell = i[2][0] - i[2][day_ago]
        profit = round((((i[2][day_ago] - i[2][0])/i[2][0])*100), 1)
        price_EP = round(i[2][0],2)
        price_OU = round(i[2][day_ago],2)
        i.append(profit_buy)
        i.append(profit_sell)
        i.append(profit)
        i.append(price_EP)
        i.append(price_OU)
        i.append(countr)


    return symbol_list
def Get_favorit_trade():
    list_symbols = Get_favorit_assets()
    history_list = Get_historical_data_of_symbols_from_yfinance(list_symbols, 30)
    history_list = Get_profit_of_list(history_list, 30)
    return history_list

def Chart_all_favorit_assets(day_ago, Side='Buy'):
    day_ago = day_ago - 1
    list_symbols = Get_favorit_assets()
    history_list = Get_historical_data_of_symbols_from_yfinance(list_symbols, 30)
    Multi_trade_road = []
    if Side == 'buy':
        for i in history_list:
            profit_change_for_symbols = []
            for j in range(day_ago, -1, -1):
                profit = ((i[2][day_ago] - i[2][j])/i[2][day_ago])*100
                profit_change_for_symbols.append([i[1], (day_ago-j), profit])
            Multi_trade_road.append(profit_change_for_symbols)
    else:
        for i in history_list:
            profit_change_for_symbols = []
            for j in range(day_ago, -1, -1):
                profit = ((i[2][j]-i[2][day_ago])/i[2][day_ago])*100
                profit_change_for_symbols.append([i[1], (day_ago-j), profit])
            Multi_trade_road.append(profit_change_for_symbols)
    return Multi_trade_road
def Chart_one_favorit_asset(day_ago, index):
    day_ago = day_ago - 1
    list_symbols = [["GC=F", 'Xau'], ["CL=F", 'Oil'], ["SI=F", 'Xag'], ["BTC-USD", 'Btc'], ["^DJI", 'Dji']]
    list_symbols = Get_favorit_assets_limit_id(int(index))
    history_list = Get_historical_data_of_symbols_from_yfinance(list_symbols, 30)
    print(history_list)
    Multi_trade_road = []
    for i in history_list:
        profit_change_for_symbols = []
        for j in range(day_ago, -1, -1):
            profit = ((i[2][day_ago] - i[2][j])/i[2][day_ago])*100
            profit_change_for_symbols.append([i[1], (day_ago-j), profit])
        Multi_trade_road.append(profit_change_for_symbols)

    return Multi_trade_road[0]

def Insert_Trade_History_F(symbol, name):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='ya mahdi',
                                             database="iran_socket")
        cursor = connection.cursor()
        sql_select_query = """INSERT INTO F_trade (id, symbol, name) VALUES(%s, %s, %s)"""
        # set variable in query
        cursor.execute(sql_select_query, (None, symbol, name, ))

        # fetch result
        connection.commit()
        print("Record inserted successfully into IT_products table")
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def Get_favorit_assets():
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='ya mahdi',
                                             database="iran_socket")
        cursor = connection.cursor()
        sql_select_query = """select * from F_trade"""
        # set variable in query
        cursor.execute(sql_select_query)
        # fetch result
        record = cursor.fetchall()
        list_lab = []
        for i in range(0, len(record)):
            list_lab_lab = []
            list_lab_lab.append(record[i][1])
            list_lab_lab.append(record[i][2])
            list_lab_lab.append(record[i][0])
            list_lab.append(list_lab_lab)
        print(list_lab)
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return list_lab
def Get_favorit_assets_limit_id(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='ya mahdi',
                                             database="iran_socket")
        cursor = connection.cursor()
        sql_select_query = """select * from F_trade where id = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
        # fetch result
        record = cursor.fetchall()
        list_lab = []
        for i in range(0, len(record)):
            list_lab_lab = []
            list_lab_lab.append(record[i][1])
            list_lab_lab.append(record[i][2])
            list_lab_lab.append(record[i][0])
            list_lab.append(list_lab_lab)
        print(list_lab)
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return list_lab
def Trade_Delet_F(ids):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='ya mahdi',
                                             database="iran_socket")
        cursor = connection.cursor()
        # Delete a record
        sql_Delete_query = """Delete from F_trade where id = %s"""
        cursor.execute(sql_Delete_query, (ids,))
        connection.commit()
        print('number of rows deleted', cursor.rowcount)
    except mysql.connector.Error as error:
        print("Failed to delete record from table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
#print(Chart_all_favorit_assets(30, 2))
#Chart_all_favorit_assets(30, 'Buy')