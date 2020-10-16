import socket
import requests
import json

from btseauth_spot import make_headers, BTSE_Endpoint

# works on testnet

#  "clOrderID": "MYOWNORDERID"
## Delete an order
cancel_params = {'orderID': 'dac5fa04-e419-4054-8fc3-1ed922d595c1', 
                 'symbol': 'BTC-USD'}

#cancel_params = {'clOrderID': 'MYOWNORDERID', 
#                 'symbol': 'BTC-USD'}


path = '/api/v3.1/order'
r = requests.delete(
    BTSE_Endpoint+ path,
    params=cancel_params,
    headers=make_headers(path, '')
)
print (BTSE_Endpoint + path )
print(r.text)
print(r.json())

'''
response:
https://testapi.btse.io/spot/api/v3.1/order

{"errorCode":404,"message":"NOTFOUND: 
orderID 00fbfa28-1d32-4801-a926-1af0b88527d4 doesn't exist.",
"status":404}

[{'status': 6, 'symbol': 'BTC-USD', 'orderType': 76,
    'price': 7010.0, 'side': 'BUY', 'size': 0.002,
    'orderID': 'b0f4f063-8a81-41fd-86f6-c8e878ac7454',
    'timestamp': 1601585924998, 'triggerPrice': 0.0, 
    'stopPrice': None, 'trigger': False, 'message': '', 
    'averageFillPrice': 0.0, 'fillSize': 0.0, 'clOrderID': 'MYOWNORDERID', 
    'stealth': 1.0, 'deviation': 1.0}]

'''
'''
success cancel

https://testapi.btse.io/spot/api/v3.1/order
[{"status":6,"symbol":"BTC-USD","orderType":76,"price":7010.0,"side":"BUY","size":0.002,"orderID":"9b96f241-32c3-4610-9a31-553633632db4","timestamp":1601537588875,"triggerPrice":0.0,"stopPrice":null,"trigger":false,"message":"","averageFillPrice":0.0,"fillSize":0.0,"clOrderID":"","stealth":1.0,"deviation":1.0}]

[{'status': 6, 
'symbol': 'BTC-USD', 
'orderType': 76, 
'price': 7010.0, 
'side': 'BUY', 
'size': 0.002, 
'orderID': '9b96f241-32c3-4610-9a31-553633632db4', 
'timestamp': 1601537588875, 
'triggerPrice': 0.0, 
'stopPrice': None, 
'trigger': False,
'message': '', 
'averageFillPrice': 0.0, 
'fillSize': 0.0, 
'clOrderID': '', 
'stealth': 1.0, 
'deviation': 1.0}]

'''