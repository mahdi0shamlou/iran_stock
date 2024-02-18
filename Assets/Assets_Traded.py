import datetime
from mysql.connector import connect, Error
import mysql.connector
from tsetmc_api.symbol import Symbol
def Get_Symbol_History(symbol_id):
    symbol = Symbol(symbol_id=symbol_id)
    price_overview = symbol.get_daily_history()
    print(price_overview[0]['close'])
    return price_overview
def Get_Trade_History():
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='ya mahdi',
                                             database="iran_socket")
        cursor = connection.cursor()
        sql_select_query = """select * from events"""
        # set variable in query
        cursor.execute(sql_select_query)
        # fetch result
        record = cursor.fetchall()
        list_lab = []
        for i in range(0, len(record)):
            list_lab_lab = []
            list_lab_lab.append(record[i][0])
            list_lab_lab.append(record[i][1])
            list_lab_lab.append(record[i][2])
            list_lab_lab.append(record[i][3])
            list_lab_lab.append(record[i][4])
            list_lab_lab.append(record[i][5])
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
def Insert_Trade_History(symbol, side):
    try:
        price_overview = Get_Symbol_History(symbol)
        if side == 'buy':
            profits = price_overview[0]['close'] - price_overview[30]['close']
        else:
            profits = price_overview[30]['close'] - price_overview[0]['close']
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='ya mahdi',
                                             database="iran_socket")
        cursor = connection.cursor()
        sql_select_query = """INSERT INTO events (id, symbol, started_at, side, price_open, profit) VALUES(%s, %s, %s, %s, %s, %s)"""
        # set variable in query
        cursor.execute(sql_select_query, (None, symbol, datetime.datetime.now(), side, price_overview[30]['close'], profits,))

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
            return 'list_lab'
    pass
Get_Trade_History()
#Insert_Trade_History(symbol='14079693677610396', side='buy')
#Get_Symbol_History('14079693677610396')
