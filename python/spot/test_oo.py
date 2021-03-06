import asyncio
import aiohttp
from btseauth_spot import make_headers, get_headers
from decimal import Decimal
import json
import time

'''
 Use this Test script to make sure that limit orders can be placed, status checked, and cancelled
 before proceeding to test in the hummingbot. It is simpler and doesn't have as many layers to check
 through. In addition the test methods here cover asyncio
'''

BTSE_Endpoint = 'https://testapi.btse.io/spot'
open_order_params = {'symbol': 'BTC-USDT'}
path = '/api/v3.2/user/open_orders'
url = BTSE_Endpoint+path

from typing import (
    Dict,
)

####
price = 574.1500000000000253769227854
price = Decimal('%.7g' % price)
limit_order_form = {"symbol": "ETH-USDT", 
                    "side": "BUY", "type": "LIMIT",
                     "price": f"{price:f}", 
                     "size": "0.09800000000000000204003480775", 
                     "triggerPrice": 0, "time_in_force": "GTC", 
                     "txType": "LIMIT", "clOrderID": "buy-ETH-USDT-1604374232705551"}

limit_path = '/api/v3.2/order'
limit_url = BTSE_Endpoint+path

'''
limit_order_form = {"symbol": "ETH-USDT", 
                    "side": "BUY", "type": "LIMIT",
                     "price": "574.150000", 
                     "size": "0.0980775", 
                     "triggerPrice": 0, 
                     "time_in_force": "GTC", 
                     "txType": "LIMIT", 
                     "clOrderID": "buy-ETH-USDT-1604374232705551"}
'''


'''
limit_order_form = {'symbol': 'BTC-USDT', 'side': 'BUY', 'type': 'LIMIT', 
                    'price': '17038.5', 
                    'size': '0.000123456', 
                    'triggerPrice': 0, 'time_in_force': 'GTC', 
                    'txType': 'LIMIT', 'clOrderID': 'buy-BTC-USDT-1606019854008947'}

limit_order_form = {"symbol": "BTC-USDT", "side": "BUY", "type": "LIMIT", 
                    "price": "17038.5", "size": "0.123 ", "triggerPrice": 0, 
                    "time_in_force": "GTC", "txType": "LIMIT", 
                    "clOrderID": "buy-BTC-USDT-1606020895015706"}
'''
'''
limit_order_form = {"symbol": "BTC-USDT", 
                    "side": "BUY",
                    "type": "LIMIT",
                    "price": "18038.5",
                    "size": "0.012",
                    "clOrderID": "buy-BTC-USDT-1606020895015706"}
'''


ts = int(time.time())
clientOID = "buy-BTC-USDT-" + str(ts)

limit_order_form = {"symbol": "BTC-USDT",
                    "side": "BUY", 
                    "type": "LIMIT", 
                    "price": "18038.5", 
                    "size": "0.012", 
                    "time_in_force": "GTC", 
                    "txType": "LIMIT", 
                    "clOrderID": f"{clientOID}"}


###
cancel_path = '/api/v3.2/order'

# use these dicts for deletion of open orders
def get_cancelparams(trade_msg: Dict[str, any]): 
    pairs = []
    for trade in trade_msg:
        symbol = trade['symbol']
        oid = trade['orderID']
        info = {'symbol': symbol, 'orderID': oid}
        pairs.append(info)
    return pairs

async def get_openorders(client, path, params):
    try:
        headers = get_headers(path, '')
        url = BTSE_Endpoint+path
        print(f'url: {url} params: {params} headers: {headers}')
        async with client.request('get', url=url, params=params, headers=headers) as response:
            result = await response.json()
            print(f"get_openorders: {url} ")
            return result
    except Exception as e: 
        print(e)


# make the headers and then pass into _api_request, because they are different
# for every type of request, be it buy/sell, cancel or get open orders
async def limit_order(client,
                      path, 
                      params):
    try:
        jsond = json.dumps(params)
        headers = get_headers(path, jsond)
        url = BTSE_Endpoint+path
        print(f"\n INSIDE CLIENT.POST: url: {url}, json: {jsond}, headers: {headers}\n")
        async with client.request('post', url=url, json=params, headers=headers) as response:
            r = await response.json()
            print("posting limit_order ")
            return r
    except Exception as e:
        print(f"Exception thrown as {e}")


async def cancel_orders(client, 
                        path, 
                        params):
    try:
        headers = get_headers(path, '')
        url = BTSE_Endpoint+path
        async with client.request('delete', url=url, params=params, headers=headers) as response:
            r = await response.text()
            print(" cancelling order ..... \n")
            print(r)
            return r
    except Exception as e:
        print(e)

async def cancel_all_orders(session, responses):
    for r in responses:
        print(r[0]['orderType'])
        ordertype = r[0]['orderType']
        if ordertype == 76: 
            print("order type is 76") # orderState is STATUS_ACTIVE, orderType is 76
            pairs = get_cancelparams(r)
            print(f'Total number of pairs: {len(pairs)}\n\n')
            print(pairs[0])
            cancel_tasks = []
            for p in pairs:
                task = asyncio.ensure_future(cancel_orders(client=session, path=cancel_path, params=p))
                cancel_tasks.append(task)
            responses = await asyncio.gather(*cancel_tasks)
            print(f'length of responses from cancel tasks: {len(responses)}')


async def place_orders():
    # place two orders
    tasks = []
    async with aiohttp.ClientSession() as session:
        task2 = asyncio.ensure_future(limit_order(client=session, path=limit_path, params=limit_order_form))
        tasks.append(task2)
        task3 = asyncio.ensure_future(limit_order(client=session, path=limit_path, params=limit_order_form))
        tasks.append(task3)
        responses = await asyncio.gather(*tasks)
        print(f'place order length of responses: {len(responses)} \n\n')
        print(responses)
        await session.close()


async def run(r):
    # place 2 limit orders, get open orders, cancel all open orders
    tasks = []
    await place_orders()
    async with aiohttp.ClientSession() as session:
        task = asyncio.ensure_future(get_openorders(client=session, path=path, params=open_order_params))
        tasks.append(task)
        responses = await asyncio.gather(*tasks)
        print(f'length of responses: {len(responses)} \n\n')
        print(responses)
        # cancel all open orders
        await cancel_all_orders(session, responses)
        await session.close()


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(2))
loop.run_until_complete(future)


# get_openorders: https://testapi.btse.io/spot/api/v3.2/user/open_orders 


'''
    async def fetch(url, session):
        async with session.get(url) as response:
            return await response.read()

    url = "http://example.org/{}"
    tasks = []
    # Fetch all responses within one Client session,
    # keep connection alive for all requests.

    async with aiohttp.ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        print(responses)
        await session.close()

def print_responses(result):
    print(result)
'''

