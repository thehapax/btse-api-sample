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
ping_checker = PeriodicChecker(period_ms = 30 * 1000)


async def connect_forever():
    path = '/spotWS'
    url = BTSE_WSEndpoint + path
    
    async with websockets.connect(url) as websocket:
        # Authentication
        auth_payload = json.dumps(gen_auth(keypair['API-KEY'], keypair['API-PASSPHRASE']))
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
        

        while True:
            msg = await websocket.recv()
            print(msg)
            if ping_checker.check():
                print(" sending a ping response of 2" )
                await websocket.send("2")


asyncio.get_event_loop().run_until_complete(connect_forever())
