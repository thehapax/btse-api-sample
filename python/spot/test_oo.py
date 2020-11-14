import asyncio
import aiohttp
from btseauth_spot import make_headers
from decimal import Decimal
import json


BTSE_Endpoint = 'https://testapi.btse.io/spot'
open_order_params = {'symbol': 'ETH-USDT'}
path = '/api/v3.2/user/open_orders'
url = BTSE_Endpoint+path


from typing import (
    Dict,
)

####
price = 457.1500000000000253769227854
price = Decimal('%.7g' % price)
limit_order_form = {"symbol": "ETH-USDT", "side": "BUY", "type": "LIMIT",
                     "price": f"{price:f}", 
                     "size": "0.09800000000000000204003480775", 
                     "triggerPrice": 0, "time_in_force": "GTC", 
                     "txType": "LIMIT", "clOrderID": "buy-ETH-USDT-1604374232705551"}
limit_path = '/api/v3.2/order'
limit_url = BTSE_Endpoint+path

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
        headers = make_headers(path, '')
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
        headers = make_headers(path, json.dumps(params))
        url = BTSE_Endpoint+path
        async with client.request('post', url=url, json=params, headers=headers) as response:
            r = await response.json()
            print("posting limit_order")
            return r
    except Exception as e:
        print(e)


async def cancel_orders(client, 
                        path, 
                        params):
    try:
        headers = make_headers(path, '')
        url = BTSE_Endpoint+path
        async with client.request('delete', url=url, params=params, headers=headers) as response:
            r = await response.text()
            print(" cancelling order ..... \n")
            print(r)
            return r
    except Exception as e:
        print(e)


async def run(r):
    tasks = []
    async with aiohttp.ClientSession() as session:
        task = asyncio.ensure_future(get_openorders(client=session, path=path, params=open_order_params))
        tasks.append(task)

        task2 = asyncio.ensure_future(limit_order(client=session, path=limit_path, params=limit_order_form))
        tasks.append(task2)
#        task3 = asyncio.ensure_future(limit_order(client=session, path=limit_path, params=limit_order_form))
#        tasks.append(task3)

        responses = await asyncio.gather(*tasks)
        print(f'length of responses: {len(responses)} \n\n')
        
        # cancel all open orders
        '''
        for r in responses:
            print(r[0]['orderType'])
            ordertype = r[0]['orderType']
            if ordertype == 76: 
                print("order type is 76")
                pairs = get_cancelparams(r)
                print(f'Total number of pairs: {len(pairs)}\n\n')
                print(pairs[0])
                cancel_tasks = []
                for p in pairs:
                    task = asyncio.ensure_future(cancel_orders(client=session, path=cancel_path, params=p))
                    cancel_tasks.append(task)
                responses = await asyncio.gather(*cancel_tasks)
                print(f'length of responses from cancel tasks: {len(responses)}')
        
        task = asyncio.ensure_future(get_openorders(client=session, path=path, params=open_order_params))
        tasks.append(task)
        responses = await asyncio.gather(*tasks)
        '''
        await session.close()


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(2))
loop.run_until_complete(future)


#get_openorders: https://testapi.btse.io/spot/api/v3.2/user/open_orders 


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



