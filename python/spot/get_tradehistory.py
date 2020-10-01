import requests
import json
from btseauth_spot import BTSE_Endpoint, make_headers
import pprint

pp = pprint.PrettyPrinter(indent=4)
path = '/api/v3.2/user/trade_history'

r = requests.get(BTSE_Endpoint+path,
    params={'symbol': 'BTC-USD'},
    headers=make_headers(path, ''))

pp.pprint(r.json())

'''

[   {   'base': 'BTC',
        'clOrderID': None,
        'feeAmount': 2e-06,
        'feeCurrency': 'BTC',
        'filledPrice': 10758.0,
        'filledSize': 0.002,
        'orderId': 'a0fca7aa-f014-4d27-b861-3c950f645bc3',
        'orderType': 77,
        'price': 21.516,
        'quote': 'USD',
        'realizedPnl': 0.0,
        'serialId': 110780426,
        'side': 'BUY',
        'size': 21.516,
        'symbol': 'BTC-USD',
        'timestamp': 1601360394000,
        'total': 0.0,
        'tradeId': 'fb21b23f-5ea0-4c7e-bede-39cf1af8816a',
        'triggerPrice': 0.0,
        'triggerType': 0,
        'username': 'hapax10test',
        'wallet': 'SPOT@'},
            .....]
            
               
'''