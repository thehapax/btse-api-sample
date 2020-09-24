import hmac
import time
import hashlib
import os 

# works on testnet and production

#Production
api_key = os.environ['BTSE_API_KEY']
api_pass = os.environ['BTSE_SECRET_KEY']

# production
#BTSE_Endpoint = 'https://api.btse.com/spot'
#BTSE_WSEndpoint = 'wss://ws.btse.com'

# Testnet
BTSE_WSEndpoint = 'wss://testws.btse.io'
BTSE_Endpoint = 'https://testapi.btse.io/spot'

#testnet tradingkey
#api_key = os.environ['BTSE_API_KEY']
#api_pass = os.environ['BTSE_SECRET_KEY']




# API Keys
keypair = {
    'API-KEY': api_key,
    'API-PASSPHRASE': api_pass
}

print("Keypair:")
print(keypair)


##Make Signature headers
def make_headers(path, data):
    nonce = str(int(time.time()*1000))
    print("nonce:" + nonce)
    message = path + nonce + data

    headers = {}
    
    signature = hmac.new(
        bytes(keypair['API-PASSPHRASE'], 'latin-1'),
        msg=bytes(message, 'latin-1'),
        digestmod=hashlib.sha384
    ).hexdigest()
    headers = {
        'btse-api':keypair['API-KEY'],
        'btse-nonce':nonce,
        'btse-sign':signature
    }
    return headers

def gen_auth(api_key, secret_key, path='/spotWS'):
    btsenonce = str(int(time.time()*1000))
    path = path + btsenonce + ''
    signature = hmac.new(
        bytes(secret_key, 'latin-1'),
        msg=bytes(path, 'latin-1'),
        digestmod=hashlib.sha384
    ).hexdigest()
    auth_payload = {
        'op': 'authKeyExpires',
        'args': [api_key, btsenonce, signature + ""]
    }
    return auth_payload    
