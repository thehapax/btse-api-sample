import socket
import requests
import json
from btseauth_spot import make_headers, BTSE_Endpoint

# Get User wallet
path = '/api/v3.2/user/wallet'
body = ''
make_headers(path,body)
r = requests.get(BTSE_Endpoint + path, headers=make_headers(path, body))
print(r.text)


