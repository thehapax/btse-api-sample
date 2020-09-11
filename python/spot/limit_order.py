import socket
import requests
import json

from btseauth_spot import BTSE_Endpoint, make_headers

# this script works on testnet
# uses REST api v3.1

## Place a limit order with price at 7010

limit_order_form = {
  "price": 7010,
  "side": "BUY",
  "size": 0.002,
  "symbol": "BTC-USD",
  "time_in_force": "GTC",
  "triggerPrice": 0,
  "txType": "LIMIT",
  "type": "LIMIT"
}

path = '/api/v3.1/order'
r = requests.post(
    BTSE_Endpoint+path,
    json=limit_order_form,
    headers=make_headers(path, json.dumps(limit_order_form))
)
print(r.text)


