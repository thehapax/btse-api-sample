import socket
import requests
import pprint 

from typing import (
    Dict,
    List,
    Optional,
    Any,
    AsyncIterable,
)


from btseauth_spot import BTSE_Endpoint, make_headers
# works on testnet
from utils import is_json

# method to check if orderID = dac5fa04-e419-4054-8fc3-1ed922d595c1 is still an openorder
def get_active_order(id, trade_msg: Dict[str, Any]):
    for open_trade in trade_msg:
        if open_trade['orderID'] == id:
            return open_trade
        

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

#res = r.text
#print(res)

''' what was this used for? 
try:
    if is_json(r.text):
        res = r.json()
        dres = res[0]
        print(dres.get('symbol'))
        pp.pprint(dres)
except IndexError as e:
    print(r.text)
'''

# all open orders 
pp.pprint(r.json())

# get just this one open order
'''
trade_msg = r.json()
order_id = 'dac5fa04-e419-4054-8fc3-1ed922d595c1'

orderinfo = get_active_order(order_id, trade_msg)
pp.pprint(orderinfo)
'''


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
