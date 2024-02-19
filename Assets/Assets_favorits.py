import yfinance as yf
def Get_historical_data_of_symbols_from_yfinance(symbol_list, day_ago=30):
    history_list = []
    for i in symbol_list:
        symbols = yf.Ticker(i[0])
        data = symbols.history(period='100d')
        #print(len(data))
        #print(data["Close"])
        #print(len(data['Close'][(len(data)-1)-day_ago:len(data)-1]))
        history_list.append([i[0], i[1], data['Close'][(len(data)-1)-day_ago:len(data)-1]])
    return history_list
def Get_profit_of_list(symbol_list, day_ago):
    day_ago = day_ago - 1
    for i in symbol_list:
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
    return symbol_list
def Get_favorit_trade():
    history_list = Get_historical_data_of_symbols_from_yfinance([["GC=F", 'Xau'], ["CL=F", 'Oil'], ["SI=F", 'Xag'], ["BTC-USD", 'Btc'], ["^DJI", 'Dji']], 30)
    history_list = Get_profit_of_list(history_list, 30)
    return history_list
    #print(history_list[0])
#print(Get_favorit_trade())