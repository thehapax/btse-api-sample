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

'''
example: 
[   {   'active': True,
        'availableSettlement': None,
        'base': 'BTC',
        'closeTime': 0,
        'contractEnd': 0,
        'contractSize': 0.0,
        'contractStart': 0,
        'fundingRate': 0.0,
        'futures': False,
        'high24Hr': 10758.0,
        'highestBid': 10757.5,
        'inactiveTime': 0,
        'last': 10758.0,
        'low24Hr': 10741.5,
        'lowestAsk': 10758.0,
        'maxOrderSize': 2000.0,
        'maxPosition': 0,
        'maxRiskLimit': 0,
        'minOrderSize': 0.001,
        'minPriceIncrement': 0.5,
        'minRiskLimit': 0,
        'minSizeIncrement': 0.001,
        'minValidPrice': 0.5,
        'openInterest': 0.0,
        'openInterestUSD': 0.0,
        'openTime': 0,
        'percentageChange': 0.00464792,
        'quote': 'USD',
        'size': 0.766,
        'startMatching': 0,
        'symbol': 'BTC-USD',
        'timeBasedContract': False,
        'volume': 8240.5455}]

'''