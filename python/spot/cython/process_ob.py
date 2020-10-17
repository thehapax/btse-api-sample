import pprint
import order_tracker
import time

def otracker(orderbook_data):
    bids = []
    asks = []
    for i in orderbook_data['buyQuote']:
        bids.append(list(i.values()))
    for i in orderbook_data['sellQuote']:
        asks.append(list(i.values()))

    ob = {'timestamp': orderbook_data['timestamp'], 'symbol': orderbook_data['symbol']}
    ob['bids'] = bids
    ob['asks'] = asks
    return ob


sample_ob = {'data': { 'buyQuote': [    {'price': '10600.0', 'size': '200.002'},
                                {'price': '10500.0', 'size': '620.000'},
                                {'price': '7000.0', 'size': '0.002'},
                                {'price': '1000.0', 'size': '1.000'},
                                {'price': '100.0', 'size': '0.003'},
                                {'price': '0.0', 'size': '34.016'}],
                'currency': 'USD',
                'sellQuote': [   {'price': '113700.0', 'size': '0.001'},
                                    {'price': '12000.0', 'size': '6.740'},
                                    {'price': '11800.0', 'size': '5095.000'},
                                    {'price': '11600.0', 'size': '185.000'},
                                    {'price': '11500.0', 'size': '525.000'},
                                    {'price': '11400.0', 'size': '75.000'},
                                    {'price': '10900.0', 'size': '38859.849'}],
                'symbol': 'BTC-USD',
                'timestamp': 1602890445777},
        'topic': 'orderBookApi:BTC-USD_5'}

def main():
    pp = pprint.PrettyPrinter(indent=4)
    
    # using cython with python
    ob = order_tracker.order_tracker(sample_ob['data'])
    pp.pprint(ob)

    #    using regular python
    obr = otracker(sample_ob['data'])
    pp.pprint(obr)


if __name__ == "__main__":
    main()