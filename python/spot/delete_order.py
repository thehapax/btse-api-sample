import socket
import requests
import json

from btseauth_spot import make_headers, BTSE_Endpoint


## Delete an order
cancel_params = {'orderID': 'd388db41-54d8-42f0-b626-8bcf7fb09cac', 'symbol': 'BTC-USD'}

path = '/api/v3.1/order'
r = requests.delete(
    BTSE_Endpoint+ path,
    params=cancel_params,
    headers=make_headers(path, '')
)
print (BTSE_Endpoint + path )
print(r.text)

