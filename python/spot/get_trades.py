import requests
from btseauth_spot import BTSE_Endpoint, make_headers
import pprint

# public orders placed for specific symbol

pp = pprint.PrettyPrinter(indent=4)

headers = {
  'Accept': 'application/json;charset=UTF-8'
}

path = '/api/v3.2/trades'

r = requests.get(BTSE_Endpoint+path,
                params={'symbol': 'BTC-USD'},
                headers = headers)

print(r.json())
