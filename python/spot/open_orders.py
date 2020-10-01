import socket
import requests
import pprint 

from btseauth_spot import BTSE_Endpoint, make_headers
# works on testnet
from utils import is_json


pp = pprint.PrettyPrinter(indent=4)
## Get Open Orders
open_order_params = {'symbol': 'BTC-USD'}

path = '/api/v3.2/user/open_orders'
headers=make_headers(path, '')
print(headers)

r = requests.get(
    BTSE_Endpoint+ path,
    params=open_order_params,
    headers=make_headers(path, '')
)
print (BTSE_Endpoint + path )

res = r.text
#print(res)

if is_json(r.text):
    res = r.json()
    dres = res[0]
    print(dres.get('symbol'))
    pp.pprint(dres)




'''
python3 open_orders.py 

https://testapi.btse.io/spot/api/v3.1/user/open_orders

[{"orderType":76,
"price":7010.0,
"size":0.002,
"side":"BUY",
"orderValue":14.02,
"filledSize":0.0,
"pegPriceMin":0.0,
"pegPriceMax":0.0,
"pegPriceDeviation":0.0,
"cancelDuration":0,
"timestamp":1600930554219,
"orderID":"11edaa79-7f16-4526-a5d6-d59134072a56",
"triggerOrder":false,
"triggerPrice":0.0,
"triggerOriginalPrice":0.0,
"triggerOrderType":0,
"triggerTrailingStopDeviation":0.0,
"triggerStopPrice":0.0,
"symbol":"BTC-USD",
"trailValue":0.0,
"averageFillPrice":0.0,
"fillSize":0.0,
"clOrderID":null,
"orderState":"STATUS_ACTIVE",
"triggered":false}]

'''
