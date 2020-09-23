import asyncio
import ujson
import hmac
import hashlib
import time
import websockets

from btseauth_spot import gen_auth, keypair, BTSE_WSEndpoint
from PeriodicChecker import PeriodicChecker
import pprint

# works on testnet and production

# ping checker for keep alive with websocket, aka heartbeat
#ping_checker = PeriodicChecker(period_ms = 30 * 1000)
ping_checker = PeriodicChecker(period_ms = 8 * 1000)
pp = pprint.PrettyPrinter(indent=4)

async def connect_forever():
    path = '/spotWS'
    url = BTSE_WSEndpoint + path
    
    async with websockets.connect(url) as websocket:
        # Authentication
        auth = gen_auth(keypair['API-KEY'], keypair['API-PASSPHRASE'])
        print("***** GEN AUTH: *****" + str(auth))
        auth_payload = ujson.dumps(auth)
        await websocket.send(auth_payload)

        # Subscription
        # notificationApi is private data
        payload = {'op': 'subscribe',
                   'args': ['notificationApiV1']}

        print("sending subscription V1 payload")
        await websocket.send(ujson.dumps(payload))
        
        '''
        # Order book subscription, 5 levels 
        payload = {
            "op":"subscribe",
            "args":["orderBookApi:BTC-USD_5"]
        }
        print("sending order book btc-usd-5 payload")
        await websocket.send(ujson.dumps(payload))
        '''        
        
        # combined tradehistory and orderbook api
        # tradehistory is public data
        payload = {
            "op":"subscribe",
            "args":["tradeHistoryApi:BTC-USDT"]
        }
        await websocket.send(ujson.dumps(payload))
        
        MESSAGE_TIMEOUT = 30.0
        PING_TIMEOUT = 10.0

        while True:
            try:
                raw_msg_str: str = await asyncio.wait_for(websocket.recv(), timeout=MESSAGE_TIMEOUT)
                print("\n ======= RECEIVED: ")
                if 'topic' in raw_msg_str:
                    x = ujson.loads(str(raw_msg_str))  # make the string a dict
                    pp.pprint(x)
                else:
                    print(raw_msg_str)
            except Exception as e:
                print(e)

            if ping_checker.check():
                payload = {"op": "ping"}
                print("==== Keep Alive HEART BEAT === sending a ping: " + str(payload))
                await websocket.send(ujson.dumps(payload))


asyncio.get_event_loop().run_until_complete(connect_forever())
