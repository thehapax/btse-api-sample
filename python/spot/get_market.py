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

#params = {'symbol': 'ETH-USDT'}
params = {'symbol': 'BTC-USDT'}
BTSE_Endpoint = 'https://testapi.btse.io/spot'

r = requests.get(BTSE_Endpoint+'/api/v3.2/market_summary', params=params, headers = headers)
#res = r.json()[0]



'''
print("----")
pp.pprint(res)
print("----")

minPrice = res.get('minPriceIncrement')  # type is float
minSize = res.get('minSizeIncrement')  # type is float
print(str(params))

print("minPriceIncrement: " + str(minPrice))
print("minSizeIncrement: " + str(minSize))
'''

print("==========>>>>>>>>>>")
pp.pprint(r.json())



'''
from market exchange crypto.com example
result[trading_pair] = TradingRule(trading_pair,
                                  min_price_increment=price_step,
                                  min_base_amount_increment=quantity_step)
'''


'''
example: 
[   {   'active': True,
        'availableSettlement': None,
        'base': 'BTC',  ### ---- base
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
        
        'minOrderSize': 0.001, # ------
        'minPriceIncrement': 0.5,  ##  xxxxxxxx
        'minRiskLimit': 0,
        'minSizeIncrement': 0.001, ## xxxxxx
        
        'minValidPrice': 0.5,
        'openInterest': 0.0,
        'openInterestUSD': 0.0,
        'openTime': 0,
        'percentageChange': 0.00464792,
        'quote': 'USD', # ----- quote 
        'size': 0.766,
        'startMatching': 0,
        'symbol': 'BTC-USD', # --------
        'timeBasedContract': False,
        'volume': 8240.5455}]
'''

'''
crypto.com get markets
 Response Example:
        {
            "id": 11,
            "method": "public/get-instruments",
            "code": 0,
            "result": {
                "instruments": [
                      {
                        "instrument_name": "ETH_CRO",
                        "quote_currency": "CRO",
                        "base_currency": "ETH",
                        "price_decimals": 2,
                        "quantity_decimals": 2
                      },
                      {
                        "instrument_name": "CRO_BTC",
                        "quote_currency": "BTC",
                        "base_currency": "CRO",
                        "price_decimals": 8,
                        "quantity_decimals": 2
                      }
                    ]
              }
        }
'''