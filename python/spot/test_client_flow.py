import json
import aiohttp
import asyncio
import pprint 
from typing import (
    Dict,
)
from btseauth_spot import BTSE_Endpoint, make_headers
from access_methods import BtseEx # get_openorders, limit_order, del_order
from decimal import Decimal
from async_utils import safe_gather


pp = pprint.PrettyPrinter(indent=4)

price = 457.1500000000000253769227854
price = Decimal('%.7g' % price)
limit_order_form = {"symbol": "ETH-USDT", "side": "BUY", "type": "LIMIT",
                     "price": f"{price:f}", 
                     "size": "0.09800000000000000204003480775", 
                     "triggerPrice": 0, "time_in_force": "GTC", 
                     "txType": "LIMIT", "clOrderID": "buy-ETH-USDT-1604374232705551"}
limit_path = 'order'
open_order_params = {'symbol': 'ETH-USDT'}


async def main():
    try:
        be = BtseEx()
        #await be.open_orders(open_order_params)
        await be.limit_order(path=limit_path, params=limit_order_form)
    except Exception as e:
        print(e)    

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# 0.250-sleep to allow underlying connections to close
loop.run_until_complete(asyncio.sleep(0.250))
loop.close()



'''
async def read_website():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://example.org/') as resp:
            return await resp.read()

loop = asyncio.get_event_loop()
loop.run_until_complete(read_website())
# 0.250-sleep to allow underlying connections to close
loop.run_until_complete(asyncio.sleep(0.250))
loop.close()

'''


