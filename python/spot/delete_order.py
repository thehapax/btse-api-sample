import socket
import requests
import json

from btseauth_spot import make_headers, BTSE_Endpoint

# works on testnet

## Delete an order
cancel_params = {'orderID': '00fbfa28-1d32-4801-a926-1af0b88527d4', 'symbol': 'BTC-USD'}

path = '/api/v3.1/order'
r = requests.delete(
    BTSE_Endpoint+ path,
    params=cancel_params,
    headers=make_headers(path, '')
)
print (BTSE_Endpoint + path )
print(r.text)

