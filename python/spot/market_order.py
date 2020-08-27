import socket
import requests
import json

from btseauth_spot import make_headers, BTSE_Endpoint


# need to fix - error on testnet
# {"errorCode":400,"message":"BADREQUEST: Size and Price should not be mixed","status":400}

## Place a market order
mkt_order_form = {
  "price": 7000,
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

