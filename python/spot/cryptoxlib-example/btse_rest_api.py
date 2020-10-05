import logging
import os

from cryptoxlib.CryptoXLib import CryptoXLib
from cryptoxlib.Pair import Pair
from cryptoxlib.version_conversions import async_run

LOG = logging.getLogger("cryptoxlib")
LOG.setLevel(logging.DEBUG)
LOG.addHandler(logging.StreamHandler())

print(f"Available loggers: {[name for name in logging.root.manager.loggerDict]}")


async def run():
    try:
        api_key = os.environ['BTSE_API_KEY']
        sec_key = os.environ['BTSE_SECRET_KEY']

        client = CryptoXLib.create_btse_client(api_key, sec_key)
    #    print("Exchange details:")
    #    await client.get_exchange_info(pair = Pair('BTC', 'USD'))

        print("Account funds:")
        await client.get_funds()
        await client.close()
    except Exception as e:
        pass
        # print(e)


if __name__ == "__main__":
    async_run(run())
