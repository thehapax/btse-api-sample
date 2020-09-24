import socket
import requests
import json
from btseauth_spot import make_headers, BTSE_Endpoint

# doesn't seem to work with testnet or production? no authorization for api key

# Get User wallet - needs authentication
'''
path = '/api/v3.2/user/wallet'
body = ''
make_headers(path,body)
r = requests.get(BTSE_Endpoint + path, headers=make_headers(path, body))
print(r.text)
'''

path = '/api/v3.1/user/wallet'

#btse_url = 'https://api.btse.com/spot'
btse_test_url = 'https://testapi.btse.io/spot'

headers=make_headers(path, '')
params = {"currency": "BTC"}

#path = '/api/v3.1/order'
r = requests.post(
    btse_test_url,
    params=params,
    headers=make_headers(path, json.dumps(params)))

print(r.json())

