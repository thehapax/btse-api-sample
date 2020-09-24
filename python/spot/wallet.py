import socket
import requests
import json
from btseauth_spot import make_headers, BTSE_Endpoint

#path = '/api/v2/user/wallet_history'

path = '/api/v3.2/user/wallet'
btse_test_url ='https://testapi.btse.io/spot/api/v3.2/user/wallet'

headers=make_headers(path, '')
params ={}

r = requests.get(
    btse_test_url,
    params=params,
    headers=headers)

print(str(r))
print(r.json())


'''

r = requests.get('https://testapi.btse.io/spot/api/v3.2/user/wallet', 
    params={}, headers = headers)

'''