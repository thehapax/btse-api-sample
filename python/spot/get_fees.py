import requests
import json
from btseauth_spot import BTSE_Endpoint, make_headers

path = '/api/v3.2/user/fees'

r = requests.get(BTSE_Endpoint+path,
    params={'symbol': 'BTC-USD'},
    headers=make_headers(path, ''))

print(r.json())