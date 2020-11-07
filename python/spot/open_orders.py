import requests
import json
import aiohttp
import asyncio
import pprint 
from typing import (
    Dict,
)
from btseauth_spot import BTSE_Endpoint, make_headers
from utils import is_json

pp = pprint.PrettyPrinter(indent=4)
open_order_params = {'symbol': 'ETH-USDT'}
path = '/api/v3.2/user/open_orders'
url = BTSE_Endpoint+path

# method to check if orderID = dac5fa04-e419-4054-8fc3-1ed922d595c1 is still an openorder
def get_active_order(id, trade_msg: Dict[str, any]):
    for open_trade in trade_msg:
        if open_trade['orderID'] == id:
            return open_trade

def get_openorders_r():
    # get open orders using requests
    r = requests.get(
        BTSE_Endpoint+ path,
        params=open_order_params,
        headers=make_headers(path, '')
    )
    # all open orders 
    print("\nAll open Orders:")
    pp.pprint(r.json())
    

async def get_openorders(url, params, headers):
    client = aiohttp.ClientSession()
    try:    
        async with client.get(url, params=params, headers=headers) as response:
            # print(await response.text())
            result = await response.text()
            parsed = json.loads(result)
            pp.pprint("\nParsed:")
            pp.pprint(parsed)
    except Exception as e: 
        print(e)
    finally:
        await client.close()


async def main():
    headers = make_headers(path, '')
    print(f'PARAMS: {open_order_params}\n')
    await get_openorders(url=url, params=open_order_params, headers=headers)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


''' what was this used for? 
try:
    if is_json(r.text):
        res = r.json()
        dres = res[0]
        print(dres.get('symbol'))
        pp.pprint(dres)
except IndexError as e:
    print(r.text)
'''


# get just this one open order
'''
trade_msg = r.json()
order_id = 'dac5fa04-e419-4054-8fc3-1ed922d595c1'

orderinfo = get_active_order(order_id, trade_msg)
pp.pprint(orderinfo)


EXAMPLE RESPONSE for open orders: 10/10/2020

[   {   'averageFillPrice': 0.0,
        'cancelDuration': 0,
        'clOrderID': 'MYOWNORDERID2',
        'fillSize': 0.0,
        'filledSize': 0.0,
        'orderID': 'cb2d5a05-357d-425a-b965-789d2727fb5a',
        'orderState': 'STATUS_ACTIVE',
        'orderType': 76,
        'orderValue': 14.1,
        'pegPriceDeviation': 0.0,
        'pegPriceMax': 0.0,
        'pegPriceMin': 0.0,
        'price': 7050.0,
        'side': 'BUY',
        'size': 0.002,
        'symbol': 'BTC-USD',
        'timestamp': 1602376422318,
        'trailValue': 0.0,
        'triggerOrder': False,
        'triggerOrderType': 0,
        'triggerOriginalPrice': 0.0,
        'triggerPrice': 0.0,
        'triggerStopPrice': 0.0,
        'triggerTrailingStopDeviation': 0.0,
        'triggered': False},
    {   'averageFillPrice': 0.0,
        'cancelDuration': 0,
        'clOrderID': 'MYOWNORDERID',
        'fillSize': 0.0,
        'filledSize': 0.0,
        'orderID': '4d607bd2-2da3-49ad-b6e7-88cf187386e7',
        'orderState': 'STATUS_ACTIVE',
        'orderType': 76,
        'orderValue': 14.02,
        'pegPriceDeviation': 0.0,
        'pegPriceMax': 0.0,
        'pegPriceMin': 0.0,
        'price': 7010.0,
        'side': 'BUY',
        'size': 0.002,
        'symbol': 'BTC-USD',
        'timestamp': 1602376395636,
        'trailValue': 0.0,
        'triggerOrder': False,
        'triggerOrderType': 0,
        'triggerOriginalPrice': 0.0,
        'triggerPrice': 0.0,
        'triggerStopPrice': 0.0,
        'triggerTrailingStopDeviation': 0.0,
        'triggered': False},
    {   'averageFillPrice': 0.0,
        'cancelDuration': 0,
        'clOrderID': 'MYOWNORDERID',
        'fillSize': 0.0,
        'filledSize': 0.0,
        'orderID': 'dac5fa04-e419-4054-8fc3-1ed922d595c1',
        'orderState': 'STATUS_ACTIVE',
        'orderType': 76,
        'orderValue': 14.02,
        'pegPriceDeviation': 0.0,
        'pegPriceMax': 0.0,
        'pegPriceMin': 0.0,
        'price': 7010.0,
        'side': 'BUY',
        'size': 0.002,
        'symbol': 'BTC-USD',
        'timestamp': 1602376392429,
        'trailValue': 0.0,
        'triggerOrder': False,
        'triggerOrderType': 0,
        'triggerOriginalPrice': 0.0,
        'triggerPrice': 0.0,
        'triggerStopPrice': 0.0,
        'triggerTrailingStopDeviation': 0.0,
        'triggered': False}]




'''



'''
python3 open_orders.py 

https://testapi.btse.io/spot/api/v3.1/user/open_orders

[{"orderType":76,
"price":7010.0,
"size":0.002,
"side":"BUY",
"orderValue":14.02,
"filledSize":0.0,
"pegPriceMin":0.0,
"pegPriceMax":0.0,
"pegPriceDeviation":0.0,
"cancelDuration":0,
"timestamp":1600930554219,
"orderID":"11edaa79-7f16-4526-a5d6-d59134072a56",
"triggerOrder":false,
"triggerPrice":0.0,
"triggerOriginalPrice":0.0,
"triggerOrderType":0,
"triggerTrailingStopDeviation":0.0,
"triggerStopPrice":0.0,
"symbol":"BTC-USD",
"trailValue":0.0,
"averageFillPrice":0.0,
"fillSize":0.0,
"clOrderID":null,
"orderState":"STATUS_ACTIVE",
"triggered":false}]

'''
