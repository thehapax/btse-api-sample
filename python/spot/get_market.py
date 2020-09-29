# get spot market summary, e.g. https://api.btse.com/spot/api/v3.2/market_summary?symbol=BTC-USD

# You can also use wget
#curl -X GET /api.btse.com/spot/api/v3.2/market_summary?symbol=string \
#  -H 'Accept: application/json;charset=UTF-8'

from btseauth_spot import BTSE_Endpoint
import requests
import pprint 

pp = pprint.PrettyPrinter(indent=4)
headers = {
  'Accept': 'application/json;charset=UTF-8'
}

r = requests.get(BTSE_Endpoint+'/api/v3.2/market_summary', params={
  'symbol': 'BTC-USD'
}, headers = headers)

pp.pprint(r.json())
