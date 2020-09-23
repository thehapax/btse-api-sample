# From BTSE Public Endpoints -
# https://www.btse.com/apiexplorer/spot/?python#btse-spot-api-public-endpoints
# get market summary, ohlcv
# get orderbook L1 and L2
# get price, trades, epoch time
import requests
import pprint

# requires symbol
market_summary = 'https://api.btse.com/spot/api/v3.2/market_summary'
ohlcv = 'https://api.btse.com/spot/api/v3.2/ohlcv'
L1 = 'https://api.btse.com/spot/api/v3.2/orderbook'
L2 = 'https://api.btse.com/spot/api/v3.2/orderbook/L2'
price = 'https://api.btse.com/spot/api/v3.2/price'
trades = 'https://api.btse.com/spot/api/v3.2/trades'

# does not require symbol
epoch_time = 'https://api.btse.com/spot/api/v3.2/time'
pp = pprint.PrettyPrinter(indent=4)
symbol = 'BTC-USD'

headers = {
  'Accept': 'application/json;charset=UTF-8'
}

def get_market(symbol):
    print("\n======= GET Market Summary ======")
    r = requests.get(market_summary, 
                    params={'symbol': symbol}, 
                    headers = headers)
    pp.pprint(r.json())
    return r.json()


def get_epochtime():
    print("\n======= GET Epoch Time ======")
    r = requests.get(epoch_time, 
                    headers = headers)
    pp.pprint(r.json())
    return r.json()


def get_l1(symbol):
    print("\n======= GET L1 Orderbook  ======")
    r = requests.get(L1, 
                    params={'symbol': symbol}, 
                    headers = headers)
    pp.pprint(r.json())
    return r.json()


def get_l2(symbol):
    print("\n======= GET L2 Orderbook ======")
    r = requests.get(L2, 
                    params={'symbol': 'BTC-USD'}, 
                    headers = headers)
    pp.pprint(r.json())
    return r.json()


def get_price(symbol):
    print("\n======= GET PRICE ======")
    r = requests.get(price, 
                    params={'symbol': symbol}, 
                    headers = headers)
    pp.pprint(r.json())
    return r.json()


def get_trades(symbol):
    print("\n======= GET TRADES ======")
    r = requests.get(trades, 
                    params={'symbol': symbol}, 
                    headers = headers)
    pp.pprint(r.json())
    return r.json()


def get_ohlcv(symbol):
    print("\n======= GET OHLCV ======")
    r = requests.get(trades, 
                    params={'symbol': symbol}, 
                    headers = headers)
    pp.pprint(r.json())
    return r.json()


def get_orderbook_data(result): # use L2 orderbook with timestamp
    bids = result['buyQuote']
    asks = result['sellQuote']
    ts = result['timestamp']
    symbol = result['symbol']
    print("==== Parsed Orderbook Data")
    print("\nSymbol: " + str(symbol))
    print("\nTimestamp: " + str(ts))
    print("\n===== BIDS =====")
    print(bids)
    print("\n===== ASKS =====")
    print(asks)
    print("side of bids array")
    print(len(bids))
    print("side of asks array")
    print(len(asks))

if __name__ == "__main__":
    '''
    result = get_epochtime()
    result = get_market(symbol)
    result = get_ohlcv(symbol)
    '''

#    result = get_l1(symbol)
    result = get_l2(symbol)
#    result = get_price(symbol)
#    result = get_trades(symbol)

    get_orderbook_data(result)

'''
result from get L2 order book

{   'buyQuote': [   {'price': '10232.0', 'size': '0.308'},
                    {'price': '10230.5', 'size': '0.199'},
                    {'price': '10228.5', 'size': '0.930'},
                    {'price': '2565.5', 'size': '0.100'}],
    'sellQuote': [   {'price': '29850.0', 'size': '1.892'},
                     {'price': '10234.0', 'size': '0.110'},
                     {'price': '10233.5', 'size': '0.302'}],
    'symbol': 'BTC-USD',
    'timestamp': 1600897059891}

'''