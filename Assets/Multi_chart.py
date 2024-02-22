from Assets.Assets_Traded import Trade_History_Chart, Get_Trade_History
from Assets.Assets_favorits import Chart_all_favorit_assets, Chart_one_favorit_asset
def Get_multi_chart_one_trade(id_trade, Side):
    Chart_list = Chart_all_favorit_assets(30, 'buy')
    trade_list = Trade_History_Chart(id_trade)
    Chart_list.append(trade_list)
    return Chart_list
def Get_multi_chart_multi_trade(id_favorits):
    list_trade = Get_Trade_History()
    Chart_list = []
    for i in list_trade:
        trade_list = Trade_History_Chart(i[0])
        Chart_list.append(trade_list)
    trade_list = Chart_one_favorit_asset(30, id_favorits)
    Chart_list.append(trade_list)
    return Chart_list


