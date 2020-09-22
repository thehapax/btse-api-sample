import asyncio
import json
import hmac
import hashlib
import time
import websockets

from btseauth_spot import gen_auth, keypair, BTSE_WSEndpoint
from PeriodicChecker import PeriodicChecker

# works on testnet and production

# ping checker for keep alive with websocket, aka heartbeat
#ping_checker = PeriodicChecker(period_ms = 30 * 1000)
ping_checker = PeriodicChecker(period_ms = 8 * 1000)

async def connect_forever():
    path = '/spotWS'
    url = BTSE_WSEndpoint + path
    
    async with websockets.connect(url) as websocket:
        # Authentication
        auth = gen_auth(keypair['API-KEY'], keypair['API-PASSPHRASE'])
        print("***** GEN AUTH: *****" + str(auth))
        auth_payload = json.dumps(auth)
        await websocket.send(auth_payload)

        # Subscription
        # notificationApi is private data
        payload = {'op': 'subscribe',
                   'args': ['notificationApiV1']}

        print("sending subscription V1 payload")
        await websocket.send(json.dumps(payload))
        
        # Order book subscription, 5 levels 
        payload = {
            "op":"subscribe",
            "args":["orderBookApi:BTC-USD_5"]
        }
        print("sending order book btc-usd-5 payload")
        await websocket.send(json.dumps(payload))
                
        ''''
        # combined tradehistory and orderbook api
        # tradehistory is public data
        payload = {
            "op":"subscribe",
            "args":["orderBookApi:BTC-USD_1", "tradeHistoryApi:BTC-USD"]
        }
        await websocket.send(json.dumps(payload))
        '''
        
        MESSAGE_TIMEOUT = 30.0
        PING_TIMEOUT = 10.0

        while True:
            raw_msg_str: str = await websocket.recv()
#            raw_msg_str: str = await asyncio.wait_for(websocket.recv(), timeout=MESSAGE_TIMEOUT)
            print("RECEIVED: " + raw_msg_str)
            #msg = await websocket.recv()
            #print(msg)
            if ping_checker.check():
                payload = {"op": "ping"}
                print("==== Keep Alive HEART BEAT === sending a ping: " + str(payload))
                await websocket.send(json.dumps(payload))


asyncio.get_event_loop().run_until_complete(connect_forever())
