import datetime
from mysql.connector import connect, Error
import mysql.connector
from tsetmc_api.symbol import Symbol
day_ago = 30
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
            list_lab_lab.append(int((record[i][5]/record[i][4])*100))

            if record[i][3] == 'buy':
                list_lab_lab.append(record[i][4]+record[i][5])
            else:
                list_lab_lab.append(record[i][4]-record[i][5])
            #print()
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
            profits = price_overview[0]['close'] - price_overview[day_ago]['close']
        else:
            profits = price_overview[day_ago]['close'] - price_overview[0]['close']
            print(price_overview[30]['close'])
            print(price_overview[0]['close'])



        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='ya mahdi',
                                             database="iran_socket")
        cursor = connection.cursor()
        sql_select_query = """INSERT INTO events (id, symbol, started_at, side, price_open, profit) VALUES(%s, %s, %s, %s, %s, %s)"""
        # set variable in query
        cursor.execute(sql_select_query, (None, symbol, datetime.datetime.now(), side, price_overview[day_ago]['close'], profits,))

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

def Trade_Update():
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='ya mahdi',
                                             database="iran_socket")
        cursor = connection.cursor()
        list_trade = Get_Trade_History()
        for i in list_trade:
            price_overview = Get_Symbol_History(i[1])
            '''
            if i[3] == 'buy':
                profit = price_overview[0]['close'] - i[4]
            else:
                profit = i[4] - price_overview[0]['close']
            '''
            if i[3] == 'buy':
                profit = price_overview[0]['close'] - price_overview[day_ago]['close']
            else:
                profit = price_overview[day_ago]['close'] - price_overview[0]['close']
            if profit != i[5] or i[4] != price_overview[day_ago]['close']:
                sql_update_query = """Update events set profit = %s, price_open = %s where id = %s"""
                # print(str(data[5]))
                input_data = (profit, i[4], i[0],)
                cursor.execute(sql_update_query, input_data)
                connection.commit()
                print(f"Record Updated successfully {i[0]}")
            else:
                print(f'Did not Updated {i[0]}')


    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def Trade_Delet(id):
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='ya mahdi',
                                             database="iran_socket")
        cursor = connection.cursor()
        # Delete a record
        sql_Delete_query = """Delete from events where id = %s"""
        cursor.execute(sql_Delete_query, (id,))
        connection.commit()
        print('number of rows deleted', cursor.rowcount)
    except mysql.connector.Error as error:
        print("Failed to delete record from table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
#Get_Trade_History()
#Trade_Update()
#Insert_Trade_History(symbol='14079693677610396', side='sell')
#Get_Symbol_History('14079693677610396')
