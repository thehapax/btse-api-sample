import socket
import requests
import json

from btseauth_spot import make_headers, BTSE_Endpoint

# works on testnet

'''
 For Market Orders, you will get this errorCode: 400 if you try to use both size and price. 
 So pick one and stick with it. For example, "just the "size" 0.002 btc will do just 
 fine as below, with price commented out. 

 {"errorCode":400,"message":"BADREQUEST: Size and Price should not be mixed","status":400}

'''

## Place a market order
mkt_order_form = {
#  "price": 7000,
  "side": "BUY",
  "size": 0.002,
  "symbol": "BTC-USD",
  "txType": "LIMIT",
  "type": "MARKET"
}

path = '/api/v3.1/order'
r = requests.post(
    BTSE_Endpoint+path,
    json=mkt_order_form,
    headers=make_headers(path, json.dumps(mkt_order_form))
)
print(r.text)

'''
response from requests: 

[{"status":4,
"symbol":"BTC-USD",
"orderType":77,
"price":10758.0,
"side":"BUY",
"size":21.516,
"orderID":"a0fca7aa-f014-4d27-b861-3c950f645bc3",
"timestamp":1601360394360,
"triggerPrice":0.0,
"stopPrice":null,
"trigger":false,
"message":"",
"averageFillPrice":10758.0,
"fillSize":0.002,
"clOrderID":"",
"stealth":1.0,
"deviation":1.0}]

'''