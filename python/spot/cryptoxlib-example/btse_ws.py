import logging
import os

from cryptoxlib.CryptoXLib import CryptoXLib
from cryptoxlib.Pair import Pair
from cryptoxlib.clients.btse.BtseWebsocket import AccountSubscription, OrderbookL2Subscription, OrderbookSubscription, \
    TradeSubscription
from cryptoxlib.version_conversions import async_run

LOG = logging.getLogger("cryptoxlib")
LOG.setLevel(logging.DEBUG)
LOG.addHandler(logging.StreamHandler())

print(f"Available loggers: {[name for name in logging.root.manager.loggerDict]}\n")


async def order_book_update(response: dict) -> None:
    print(f"Callback order_book_update: [{response}]")


async def run():
    api_key = os.environ['BTSE_API_KEY']
    sec_key = os.environ['BTSE_SECRET_KEY']
    
    #client = CryptoXLib.create_btse_client(api_key, sec_key)

    client = CryptoXLib.create_btse_client(api_key, sec_key)
    
    print(" CLIENT INITIATED")
    print(str(await client.get_time()))
    print(" --- end get time --- ")


    
    # Bundle several subscriptions into a single websocket
    
#    client.compose_subscriptions([
#        AccountSubscription()       
#    ])

    client.compose_subscriptions([
        OrderbookL2Subscription([Pair("BTC", "USD"), Pair('ETH', 'BTC')], depth = 1)
    ])
    
    # Bundle another subscriptions into a separate websocket
    '''
    client.compose_subscriptions([
        OrderbookSubscription([Pair('BTSE', 'BTC')], callbacks = [order_book_update]),
        TradeSubscription([Pair('BTSE', 'BTC')])
    ])
    '''

    # Execute all websockets asynchronously
    await client.start_websockets()

if __name__ == "__main__":
    async_run(run())
