import socket
import requests
import json
import aiohttp, asyncio

from utils import get_status_msg
from btseauth_spot import BTSE_Endpoint, make_headers

# this script works on testnet
# uses REST api v3.1

## Place a limit order with price at 7010
limit_order_form = {
  "price": 7050,
  "side": "BUY",
  "size": 0.002,
  "symbol": "BTC-USDT",
  "time_in_force": "GTC",
  "triggerPrice": 0,
  "txType": "LIMIT",
  "type": "LIMIT",
  "clOrderID": "MYOWNORDERID2",
}

path = '/api/v3.1/order'
url = BTSE_Endpoint+path

# requests example
def limit_order(order_form):
  r = requests.post(
      url,
      json=order_form,
      headers=make_headers(path, json.dumps(order_form))

  )
  print(r.text)
  return r.text

# asyncio example
async def limit_order(url, params, headers):
    client = aiohttp.ClientSession()
    try:
        response = await client.post(url, json=params, headers=headers)
        r = await response.text()
        print("RESPONSE from client: " + r + "\n")
        parsed = json.loads(await response.text())
        print(f'\nParsed:\n {parsed}')
        if type(parsed) == list:
            code = parsed[0]['status']
            msg = get_status_msg(code)
            print(f'\nLimit Order Status Message: {msg}')
        else:   # error dict returned, get actual error message and return
            msg = parsed['message']
    except Exception as e:
        print(e)
    finally:
        await client.close()


async def main():
  headers=make_headers(path, json.dumps(limit_order_form))
  res = await limit_order(url, params=limit_order_form,  headers=headers)


if __name__ == '__main__':
#    limit_order(limit_order_form)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



'''
repsonse: 

nonce:1601499116289

[{"status":2,
"symbol":"BTC-USD",
"orderType":76,
"price":7010.0,
"side":"BUY",
"size":0.002,
"orderID":"9b96f241-32c3-4610-9a31-553633632db4",
"timestamp":1601499117485,
"triggerPrice":0.0,
"stopPrice":null,
"trigger":false,
"message":"",
"averageFillPrice":0.0,
"fillSize":0.0,
"clOrderID":"",
"stealth":1.0,
"deviation":1.0}]

'''