# distutils: language=c++

from libcpp.vector cimport vector

def order_tracker(orderbook_data):    
    cdef vector[float] bids
    cdef vector[float] asks
    for i in orderbook_data['buyQuote']:
        bids.push_back(i)
    for i in orderbook_data['sellQuote']:
        asks.push_back(i)

    ob = {'timestamp': orderbook_data['timestamp'], 'symbol': orderbook_data['symbol']}
    ob['bids'] = bids
    ob['asks'] = asks
    return ob

