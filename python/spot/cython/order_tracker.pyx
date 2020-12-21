# distutils: language=c++
import logging
import numpy as np

from decimal import Decimal
from typing import Dict
import time
#from hummingbot.logger import HummingbotLogger
#from hummingbot.core.data_type.order_book_row import OrderBookRow
from OrderBookRow import OrderBookRow

_active_asks = {}
_active_bids = {}

def order_tracker(orderbook_data):    
    cdef bids = []
    cdef asks = []
    for i in orderbook_data['buyQuote']:
        bids.append(list(i.values()))
    for i in orderbook_data['sellQuote']:
        asks.append(list(i.values()))

    cdef ob = {'timestamp': orderbook_data['timestamp'], 'symbol': orderbook_data['symbol']}
    ob['bids'] = bids
    ob['asks'] = asks
    return ob


cdef tuple c_convert_diff_message_to_np_arrays(object message):
    cdef:
        dict content = message.content
        list bid_entries = []
        list ask_entries = []
        str order_id
        str order_side
        str price_raw
        object price
        dict order_dict
        double timestamp = message.timestamp
        double amount = 0

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


cdef tuple c_convert_snapshot_message_to_np_arrays(object message):
    cdef:
        float price
        float amount
        str order_id
        dict order_dict

    # Refresh all order tracking.
    _active_bids.clear()
    _active_asks.clear()
    timestamp = message.timestamp
    content = message.content

    cdef c_bids = []
    cdef c_asks = []
    for i in content['buyQuote']:
        c_bids.append(list(i.values()))
    for i in content['sellQuote']:
        c_asks.append(list(i.values()))

    for snapshot_orders, active_orders in [(c_bids, _active_bids), (c_asks, _active_asks)]:
        for order in snapshot_orders:
            price, amount = get_rates_and_quantities(order)
            order_dict = {
                "order_id": timestamp,
                "amount": amount
            }
            if price in active_orders:
                active_orders[price][timestamp] = order_dict
            else:
                active_orders[price] = {
                    timestamp: order_dict
                }

    cdef:
        np.ndarray[np.float64_t, ndim=2] bids = np.array(
            [[message.timestamp,
                price,
                sum([order_dict["amount"]
                    for order_dict in _active_bids[price].values()]),
                message.update_id]
                for price in sorted(_active_bids.keys(), reverse=True)], dtype="float64", ndmin=2)
        np.ndarray[np.float64_t, ndim=2] asks = np.array(
            [[message.timestamp,
                price,
                sum([order_dict["amount"]
                    for order_dict in _active_asks[price].values()]), # correction : add _ to active_asks
                message.update_id]
                for price in sorted(_active_asks.keys(), reverse=True)], dtype="float64", ndmin=2
        )

    if bids.shape[1] != 4:
        bids = bids.reshape((0, 4))
    if asks.shape[1] != 4:
        asks = asks.reshape((0, 4))

    return bids, asks


def convert_snapshot_message_to_order_book_row(self, message):
    np_bids, np_asks = self.c_convert_snapshot_message_to_np_arrays(message)
    bids_row = [OrderBookRow(price, qty, update_id) for ts, price, qty, update_id in np_bids]
    asks_row = [OrderBookRow(price, qty, update_id) for ts, price, qty, update_id in np_asks]
    return bids_row, asks_row

