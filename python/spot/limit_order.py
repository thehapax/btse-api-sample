import socket
import requests
import json

from btseauth_spot import BTSE_Endpoint, make_headers

# this script works on testnet
# uses REST api v3.1

## Place a limit order with price at 7010

limit_order_form = {
  "price": 7050,
  "side": "BUY",
  "size": 0.002,
  "symbol": "BTC-USDT",
  "time_in_force": "GTC",
  "triggerPrice": 0,
  "txType": "LIMIT",
  "type": "LIMIT",
  "clOrderID": "MYOWNORDERID2",
}

path = '/api/v3.1/order'
r = requests.post(
    BTSE_Endpoint+path,
    json=limit_order_form,
    headers=make_headers(path, json.dumps(limit_order_form))
)
print(r.text)


'''
repsonse: 

nonce:1601499116289

[{"status":2,
"symbol":"BTC-USD",
"orderType":76,
"price":7010.0,
"side":"BUY",
"size":0.002,
"orderID":"9b96f241-32c3-4610-9a31-553633632db4",
"timestamp":1601499117485,
"triggerPrice":0.0,
"stopPrice":null,
"trigger":false,
"message":"",
"averageFillPrice":0.0,
"fillSize":0.0,
"clOrderID":"",
"stealth":1.0,
"deviation":1.0}]

'''