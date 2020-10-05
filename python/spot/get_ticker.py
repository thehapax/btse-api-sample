# get spot market summary, e.g. 
# https://api.btse.com/spot/api/v3.2/market_summary?symbol=BTC-USD

# You can also use wget
#curl -X GET /api.btse.com/spot/api/v3.2/market_summary?symbol=string \
#  -H 'Accept: application/json;charset=UTF-8'

from btseauth_spot import BTSE_Endpoint
import requests
import pprint 

from typing import (
    List,
    Dict,
    Any,
    Optional,
)

pp = pprint.PrettyPrinter(indent=4)
headers = {
  'Accept': 'application/json;charset=UTF-8'
}

r = requests.get(BTSE_Endpoint+'/api/v3.2/price', params={
#  'symbol': 'BTC-USDT'
}, headers = headers)

#pp.pprint(r.json())

all_trading_pairs: List[Dict[str, Any]] = r.json()
all_symbols = [item["symbol"] for item in all_trading_pairs]

print(all_symbols)

'''
response : 

[   {   'indexPrice': 10760.011089409,
        'lastPrice': 10760.5,
        'markPrice': 0.0,
        'symbol': 'BTC-USDT'}]
        
TICKER =  [{      'indexPrice': 10757.969784007,
                  'lastPrice': 10758.0,
                  'markPrice': 0.0,
                  'symbol': 'BTC-USD'},
            {     'indexPrice': 0.032580719,
                  'lastPrice': 0.041102,
                  'markPrice': 0.0,
                  'symbol': 'ETH-BTC'} ]
        
'''