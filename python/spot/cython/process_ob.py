import pprint
import order_tracker
import time
import numpy as np
import pprint

sample_ob = {'data': {'buyQuote': [ {'price': '10600.0', 'size': '200.002'},
                                {'price': '10500.0', 'size': '620.000'},
                                {'price': '7000.0', 'size': '0.002'},
                                {'price': '1000.0', 'size': '1.000'},
                                {'price': '100.0', 'size': '0.003'},
                                {'price': '0.0', 'size': '34.016'}],
                'currency': 'USD',
                'sellQuote': [  {'price': '113700.0', 'size': '0.001'},
                                {'price': '12000.0', 'size': '6.740'},
                                {'price': '11800.0', 'size': '5095.000'},
                                {'price': '11600.0', 'size': '185.000'},
                                {'price': '11500.0', 'size': '525.000'},
                                {'price': '11400.0', 'size': '75.000'},
                                {'price': '10900.0', 'size': '38859.849'}],
                'symbol': 'BTC-USD',
                'timestamp': 1602890445777},
        'topic': 'orderBookApi:BTC-USD_5'}

sample2_ob = {'buyQuote': [{'price': '10800.0', 'size': '0.001'}, 
                           {'price': '10596.5', 'size': '0.001'}, 
                           {'price': '10595.0', 'size': '5.000'}, 
                           {'price': '10579.5', 'size': '25.000'},
                            {'price': '10564.5', 'size': '45.000'}, 
                            {'price': '10554.5', 'size': '0.001'}, 
                            {'price': '10549.0', 'size': '65.000'}, 
                            {'price': '10531.5', 'size': '85.000'}, 
                            {'price': '10516.0', 'size': '105.000'}, 
                            {'price': '10500.5', 'size': '125.000'}, 
                            {'price': '10485.0', 'size': '145.000'}, 
                            {'price': '10452.0', 'size': '185.000'}, 
                            {'price': '9173.5', 'size': '0.001'}, 
                            {'price': '6966.5', 'size': '0.020'}, 
                            {'price': '6927.0', 'size': '0.002'}, 
                            {'price': '988.0', 'size': '1.000'}, 
                            {'price': '120.5', 'size': '0.003'},
                             {'price': '5.5', 'size': '6.000'}, 
                             {'price': '4.5', 'size': '5.000'}, 
                             {'price': '3.5', 'size': '4.000'}, 
                             {'price': '2.5', 'size': '3.000'}, 
                             {'price': '1.5', 'size': '2.000'}, 
                             {'price': '0.5', 'size': '4.002'}, 
                             {'price': '0.0', 'size': '10.012'}], 
              'sellQuote': [{'price': '114886.5', 'size': '0.001'},                             
                            {'price': '13004.0', 'size': '0.100'},
                             {'price': '12533.5', 'size': '165.000'}, 
                             {'price': '12515.5', 'size': '145.000'}, 
                             {'price': '12496.5', 'size': '125.000'}, 
                             {'price': '12478.0', 'size': '105.000'}, 
                             {'price': '12459.5', 'size': '85.000'}, 
                             {'price': '12441.0', 'size': '65.000'}, 
                             {'price': '12422.5', 'size': '45.000'}, 
                             {'price': '12403.5', 'size': '25.000'}, 
                             {'price': '12385.0', 'size': '5.000'}, 
                             {'price': '12095.0', 'size': '6.640'}, 
                             {'price': '11898.5', 'size': '5095.000'},
                              {'price': '11121.0', 'size': '0.001'}, 
                              {'price': '11018.5', 'size': '2000.000'}, 
                              {'price': '10994.0', 'size': '25859.805'}], 
              'timestamp': 1603262633077, 
              'symbol': 'BTC-USDT', 
              'trading_pair': 'BTC-USDT'}


# reformat to this dict format: 
cc_example =  {
        "bids": [[
            11746.488,    # price
            128,          # quantity
            8             # number of Orders
          ]
        ],
        "asks": [
          [
            11747.488,    # price
            201,          # quantity
            12            # number of Orders
          ]
        ],
        "t": 1587523078844
      }

# {   "bids":[[9668.44,0.006325,1.0],[9659.75,0.006776,1.0]],
#    "asks":[[9697.0,0.68251,1.0],[9697.6,1.722864,2.0]],
#   "t":1591704180270 }


def otracker(orderbook_data):
    bids = []
    asks = []
    for i in orderbook_data['buyQuote']:
        bids.append(list(i.values()))
    for i in orderbook_data['sellQuote']:
        asks.append(list(i.values()))
    return bids, asks

def reshape(orderbook_data):
    newob = {}
    bids = []
    asks = []
    t = orderbook_data['timestamp']
    for i in orderbook_data['buyQuote']:
        bids.append(list(i.values()))
    for i in orderbook_data['sellQuote']:
        asks.append(list(i.values()))
    newob = {'bids': bids, 'asks': asks, 't': t}
    return newob


def get_rates_and_quantities(entry) -> tuple:
    # price, quantity
    items =  list(entry.values())
    return float(items[0]), float(items[1])


def diff_message(content):
    s_empty_diff = np.ndarray(shape=(0, 4), dtype="float64")

    bid_entries = content['buyQuote']
    ask_entries = content['sellQuote']
    
    for e in bid_entries:
        a,b = get_rates_and_quantities(e)
        print(a,b)
    
    bids = s_empty_diff
    asks = s_empty_diff
    update_id = 1
    timestamp = time.time()
    print(f"timestamp {timestamp} ")

    if len(bid_entries) > 0:
            bids = np.array(
                [[timestamp,
                  float(price),
                  float(amount),
                  update_id]
                 for price, amount in [get_rates_and_quantities(entry) for entry in bid_entries]],
                dtype="float64",
                ndmin=2
            )
            
    if len(ask_entries) > 0:
        asks = np.array(
            [[timestamp,
                float(price),
                float(amount),
                update_id]
                for price, amount in [get_rates_and_quantities(entry) for entry in ask_entries]],
            dtype="float64",
            ndmin=2
        )

    return bids, asks


def main():
    
    pp = pprint.PrettyPrinter(indent=4)
    '''
    bids, asks = diff_message(sample_ob['data'])
    pp.pprint(bids)
    pp.pprint(asks)
    '''
    '''
    pp.pprint(sample_ob['data']['timestamp'])
    # using cython with python
    print("cython with python")
    ob = order_tracker.order_tracker(sample_ob['data'])
    pp.pprint(ob)
    '''
    '''
    # using regular python
    print("python only")
    bids, asks = otracker(sample_ob['data'])
    pp.pprint(bids)
    pp.pprint(asks)
    '''
    
    newbook = reshape(sample_ob['data'])
    pp.pprint(newbook)
    

if __name__ == "__main__":
    main()
    
    
'''
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
'''
