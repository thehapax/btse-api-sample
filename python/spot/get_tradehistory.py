import requests
import json
from btseauth_spot import BTSE_Endpoint, make_headers
import pprint

pp = pprint.PrettyPrinter(indent=4)
path = '/api/v3.2/user/trade_history'

r = requests.get(BTSE_Endpoint+path,
    params={'symbol': 'BTC-USD'},
    headers=make_headers(path, ''))

pp.pprint(r.json())