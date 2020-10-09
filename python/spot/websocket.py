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
ping_checker = PeriodicChecker(period_ms = 8 * 1000)
pp = pprint.PrettyPrinter(indent=4)


def subscription_payload():
    # notificationApi is private data
    payload = {'op': 'subscribe',
                'args': ['notificationApiV1']}

    print("sending subscription V1 payload")
    return payload

def orderbook_payload():
    # Order book subscription, 5 levels, public data
    payload = {
        "op":"subscribe",
        "args":["orderBookApi:BTC-USD_5"] # up to 150 entries
    }
    print("sending order book btc-usd-5 payload")
    return payload

def tradehistory_payload():
    # combined tradehistory and orderbook api
    # tradehistory is public data
    payload = {
        "op":"subscribe",
        "args":["tradeHistoryApi:BTC-USD"]
    }
    return payload

def process_orderbook_data(ob):
    bids = ob['data']['buyQuote']
    asks = ob['data']['sellQuote']
    print("===== Bids =====")
    print(bids)
    print("==== Asks =====")
    print(asks)

def get_auth_responses(response):
    lookup = {'UNLOGIN_USER connect success': 'Connected No Login or bad token', 
              'connect success': 'connected with token',
              'is authenticated successfully': 'do auth pass',
              'AUTHENTICATE ERROR': 'do auth pass failed' }
    
    for k,v in lookup.items():
        if k in response:
            return v
            

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
        #payload = subscription_payload()
        #payload = orderbook_payload()
        payload = tradehistory_payload()
        await websocket.send(ujson.dumps(payload))
                       
        MESSAGE_TIMEOUT = 30.0
        PING_TIMEOUT = 10.0

        while True:
            try:
                response: Dict[Any] = await asyncio.wait_for(websocket.recv(), timeout=MESSAGE_TIMEOUT)
                print("\n ======= RECEIVED: ")

                print(type(response))
                # x = ujson.loads(str(response))
                # pp.pprint(x)
                
                if "topic" in response:
                    r = ujson.loads(str(response))  # make the string a dict
                    pp.pprint(r)
                    #process_orderbook_data(x)
                    #for trade in r["data"]:
                    #    print(trade)
                else:
                    print("no topic in response")
                    code = get_auth_responses(response)
                    print(code + ": " + response)
            except Exception as e:
                print(e)

            if ping_checker.check():
                payload = {"op": "ping"}
                print("==== Keep Alive HEART BEAT === sending a ping: " + str(payload))
                await websocket.send(ujson.dumps(payload))


asyncio.get_event_loop().run_until_complete(connect_forever())


'''
Sample result:
===== Bids =====
[{'price': '10247.0', 'size': '0.112'}, {'price': '10246.5', 'size': '0.471'}, {'price': '10246.0', 'size': '0.237'}, {'price': '10245.0', 'size': '0.319'}, {'price': '10243.5', 'size': '0.960'}, {'price': '10243.0', 'size': '1.119'}, {'price': '10242.5', 'size': '1.288'}, {'price': '10242.0', 'size': '2.521'}, {'price': '10241.5', 'size': '3.273'}, {'price': '10240.5', 'size': '0.466'}]
==== Asks =====
[{'price': '10262.5', 'size': '0.286'}, {'price': '10262.0', 'size': '0.438'}, {'price': '10258.0', 'size': '0.610'}, {'price': '10257.5', 'size': '0.198'}, {'price': '10257.0', 'size': '0.281'}, {'price': '10256.5', 'size': '0.138'}, {'price': '10256.0', 'size': '0.161'}, {'price': '10255.5', 'size': '0.304'}, {'price': '10254.5', 'size': '0.092'}, {'price': '10254.0', 'size': '0.332'}]

'''

'''

{   'data': [   {   'price': 10758.0,
                    'side': 'BUY',
                    'size': 0.092,
                    'symbol': 'BTC-USD',
                    'timestamp': 1601873979246,
                    'tradeId': 110985476},
                {   'price': 10500.0,
                    'side': 'BUY',
                    'size': 5.0,
                    'symbol': 'BTC-USD',
                    'timestamp': 1601213574958,
                    'tradeId': 110722582},
                {   'price': 10500.0,
                    'side': 'BUY',
                    'size': 25.0,
                    'symbol': 'BTC-USD',
                    'timestamp': 1601213564931,
                    'tradeId': 110722580}],
    'topic': 'tradeHistoryApi:BTC-USD'}
    
    '''