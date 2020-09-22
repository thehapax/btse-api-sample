# From Public Endpoints
# get market summary
# get ohlcv
# get orderbook L1 and L2
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


if __name__ == "__main__":
    result = get_epochtime()
    result = get_market(symbol)
    result = get_ohlcv(symbol)

    result = get_l1(symbol)
    result = get_l2(symbol)
    result = get_price(symbol)
    result = get_trades(symbol)
