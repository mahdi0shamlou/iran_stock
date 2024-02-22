from Assets.Assets_Traded import Trade_History_Chart
from Assets.Assets_favorits import Chart_all_favorit_assets
def Get_multi_chart_one_trade(id_trade, Side):
    Chart_list = Chart_all_favorit_assets(30, Side)
    trade_list = Trade_History_Chart(id_trade)
    Chart_list.append(trade_list)
    print(Chart_list)
    return Chart_list
def Get_multi_chart_multi_trade(id_favorits):
    pass

