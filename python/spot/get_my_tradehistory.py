import requests
import json
from btseauth_spot import BTSE_Endpoint, make_headers
import pprint
from decimal import Decimal
import time

_last_tracking_nonce = 0
_last_tracking_nonce_low_res = 0

# This tracking nonce is needed bc resolution for time.time() on Windows is very low (16ms),
# not good enough to create unique order_id.
def get_tracking_nonce() -> int:
    global _last_tracking_nonce
    nonce = int(time.time() * 1e6)
    _last_tracking_nonce = nonce if nonce > _last_tracking_nonce else _last_tracking_nonce + 1
    return _last_tracking_nonce

def get_tracking_nonce_low_res() -> int:
    global _last_tracking_nonce_low_res
    nonce = int(time.time() * 1e3)
    _last_tracking_nonce_low_res = nonce if nonce > _last_tracking_nonce_low_res else _last_tracking_nonce_low_res + 1
    return _last_tracking_nonce_low_res


pp = pprint.PrettyPrinter(indent=4)
path = '/api/v3.2/user/trade_history'

# 'serialId': 111129514,
# params = {}
# must use startTime in order to filter appropriately, or too much data returned
# 13 digit timestamp

#params={'symbol': 'BTC-USD',

# clOrderID': 'buy-BTC-USDT-1606020895015706'
'''
params = {'symbol': 'BTC-USDT', 
          'orderId': '7bda5bcc-68fb-459e-8376-bcd8137600c9',
          'startTime': 1602229229000 } 
'''
# 1602229229000
# 1611042043073
# 1611041950804762

params = {'symbol': 'BTC-USDT', 
         'orderId': '7bda5bcc-68fb-459e-8376-bcd8137600c9',
          'startTime': 1611040430000}
# 1611040433171
#          'startTime': get_tracking_nonce_low_res()-10000000000} 

params = {'orderId': 'a01416b4-96b7-429e-8ed4-33ee8bf06d0a',
         'startTime': 1606469000000 }

# 'timestamp': 1606469069000

print(f'Params: {params}')

fullpath = BTSE_Endpoint+path
print(f'REST API: {fullpath}')

r = requests.get(fullpath,
                params=params,
                headers=make_headers(path, ''))

result = r.json()
pp.pprint(result)



'''
Already closed Orders, that have been fully transacted. 
            
    [   {   'base': 'BTC',
        'clOrderID': None,
        'feeAmount': 2e-06,
        'feeCurrency': 'BTC',
        'filledPrice': 10758.0,
        'filledSize': 0.002,
        'orderId': 'b3a65f8e-e838-4c13-adf4-62fef98504a1',
        'orderType': 77,
        'price': 21.516,
        'quote': 'USD',
        'realizedPnl': 0.0,
        'serialId': 110947333,
        'side': 'BUY',
        'size': 21.516,
        'symbol': 'BTC-USD',
        'timestamp': 1601791330000,
        'total': 0.0,
        'tradeId': '1c062ffa-0386-4d63-8cff-c6f4de05a270',
        'triggerPrice': 0.0,
        'triggerType': 0,
        'username': 'hapax10test',
        'wallet': 'SPOT@'},
        
    {   'base': 'BTC',
        'clOrderID': None,
        'feeAmount': 2e-06,
        'feeCurrency': 'BTC',
        'filledPrice': 10758.0,
        'filledSize': 0.002,
        'orderId': '2e7e8e97-97a8-434a-8b06-a281bcdc2c6e',
        'orderType': 77,
        'price': 21.516,
        'quote': 'USD',
        'realizedPnl': 0.0,
        'serialId': 110831739,
        'side': 'BUY',
        'size': 21.516,
        'symbol': 'BTC-USD',
        'timestamp': 1601499159000,
        'total': 0.0,
        'tradeId': 'b028f5e6-b0a4-4cf5-8bbf-278bdfb5fb40',
        'triggerPrice': 0.0,
        'triggerType': 0,
        'username': 'hapax10test',
        'wallet': 'SPOT@'},
    {   'base': 'BTC',
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
    {   'base': 'BTC',
        'clOrderID': None,
        'feeAmount': 2e-06,
        'feeCurrency': 'BTC',
        'filledPrice': 10758.0,
        'filledSize': 0.002,
        'orderId': '0f424b38-82ac-43d0-8e27-804e631f6351',
        'orderType': 77,
        'price': 21.516,
        'quote': 'USD',
        'realizedPnl': 0.0,
        'serialId': 110778325,
        'side': 'BUY',
        'size': 21.516,
        'symbol': 'BTC-USD',
        'timestamp': 1601351568000,
        'total': 0.0,
        'tradeId': '6a896d74-5ec8-4e8f-bd43-6db0d9437985',
        'triggerPrice': 0.0,
        'triggerType': 0,
        'username': 'hapax10test',
        'wallet': 'SPOT@'},
    {   'base': 'BTC',
        'clOrderID': None,
        'feeAmount': 2e-06,
        'feeCurrency': 'BTC',
        'filledPrice': 10287.5,
        'filledSize': 0.002,
        'orderId': 'e35485fa-792a-4941-a4f4-488a376e2392',
        'orderType': 77,
        'price': 20.575,
        'quote': 'USD',
        'realizedPnl': 0.0,
        'serialId': 110598355,
        'side': 'BUY',
        'size': 20.575,
        'symbol': 'BTC-USD',
        'timestamp': 1600903020000,
        'total': 0.0,
        'tradeId': '71867573-0098-43ea-b7d4-1f49756fea04',
        'triggerPrice': 0.0,
        'triggerType': 0,
        'username': 'hapax10test',
        'wallet': 'SPOT@'},
    {   'base': 'BTC',
        'clOrderID': None,
        'feeAmount': 2e-06,
        'feeCurrency': 'BTC',
        'filledPrice': 10403.0,
        'filledSize': 0.002,
        'orderId': '8c9b3e27-058b-46ee-bad0-d55885ee6ec2',
        'orderType': 77,
        'price': 20.806,
        'quote': 'USD',
        'realizedPnl': 0.0,
        'serialId': 110362655,
        'side': 'BUY',
        'size': 20.806,
        'symbol': 'BTC-USD',
        'timestamp': 1600315122000,
        'total': 0.0,
        'tradeId': '154157ef-5e41-439c-bace-856de4dc0441',
        'triggerPrice': 0.0,
        'triggerType': 0,
        'username': 'hapax10test',
        'wallet': 'SPOT@'},
    {   'base': 'BTC',
        'clOrderID': None,
        'feeAmount': 2e-06,
        'feeCurrency': 'BTC',
        'filledPrice': 10403.0,
        'filledSize': 0.002,
        'orderId': '8d15144c-24f3-4a46-acec-8efe7f14f241',
        'orderType': 77,
        'price': 20.806,
        'quote': 'USD',
        'realizedPnl': 0.0,
        'serialId': 110358921,
        'side': 'BUY',
        'size': 20.806,
        'symbol': 'BTC-USD',
        'timestamp': 1600304819000,
        'total': 0.0,
        'tradeId': '76f63c7c-58e4-4c8c-8a2c-7044cb9dd1ac',
        'triggerPrice': 0.0,
        'triggerType': 0,
        'username': 'hapax10test',
        'wallet': 'SPOT@'},
    {   'base': 'BTC',
        'clOrderID': None,
        'feeAmount': 0.104025,
        'feeCurrency': 'USDC',
        'filledPrice': 10402.5,
        'filledSize': 0.01,
        'orderId': 'f3171244-5739-4ab0-b056-1e5c7b53510f',
        'orderType': 77,
        'price': 0.01,
        'quote': 'USD',
        'realizedPnl': 0.0,
        'serialId': 110358913,
        'side': 'SELL',
        'size': 0.01,
        'symbol': 'BTC-USD',
        'timestamp': 1600304751000,
        'total': 0.0,
        'tradeId': 'ad46eceb-8e1a-4a88-9c24-b27e36ff2d7d',
        'triggerPrice': 0.0,
        'triggerType': 0,
        'username': 'hapax10test',
        'wallet': 'SPOT@'},
    {   'base': 'BTC',
        'clOrderID': None,
        'feeAmount': 9.6e-05,
        'feeCurrency': 'BTC',
        'filledPrice': 10403.0,
        'filledSize': 0.096,
        'orderId': '1e367e8d-f1eb-43e7-96be-479a9eaf8847',
        'orderType': 77,
        'price': 1000.0,
        'quote': 'USD',
        'realizedPnl': 0.0,
        'serialId': 110358911,
        'side': 'BUY',
        'size': 1000.0,
        'symbol': 'BTC-USD',
        'timestamp': 1600304737000,
        'total': 0.0,
        'tradeId': '98c700b3-ec68-494d-802e-e3139e76c026',
        'triggerPrice': 0.0,
        'triggerType': 0,
        'username': 'hapax10test',
        'wallet': 'SPOT@'},
    {   'base': 'BTC',
        'clOrderID': None,
        'feeAmount': 2.0773,
        'feeCurrency': 'USDC',
        'filledPrice': 10386.5,
        'filledSize': 0.2,
        'orderId': '4c8521d0-9d96-42ad-bc2c-5bc5cd7efb3d',
        'orderType': 77,
        'price': 0.2,
        'quote': 'USD',
        'realizedPnl': 0.0,
        'serialId': 110358907,
        'side': 'SELL',
        'size': 0.2,
        'symbol': 'BTC-USD',
        'timestamp': 1600304589000,
        'total': 0.0,
        'tradeId': 'acec1771-30f5-46be-8d3b-427186ff5fa6',
        'triggerPrice': 0.0,
        'triggerType': 0,
        'username': 'hapax10test',
        'wallet': 'SPOT@'}]
               
               
               

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