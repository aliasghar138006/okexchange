
# ContentType = 'application/json'

# apikey = 37c541a1-****-****-****-10fe7a038418

# x-signature: leaVRET-****-****-****-j8gnl3uw

# x-timestamp: 1664789830555

from datetime import datetime
import base64
import hashlib
import hmac
import simplejson as json
import requests
# secretKey = '9060d58b-1686-54d6-8ef1-74653e4954f2'
# ApiKey = '4d0601d0-4181-11ee-82bc-c1fe7802e12d'

#German
secretKey = 'a7ac23fa-4242-591d-ad0e-81637b0aafc6'
ApiKey = '2142aec0-4188-11ee-82bc-c1fe7802e12d'


#coinex

# secretKey = 'F28FDA7DE3E9F761930807CB578699CEFEE219DF2DA153D5'
# ApiKey = '50A1E0B654004369B5A7A0212A2E4581'




def create_signature(secret_key, full_path, request_method, request_data=None):
    timestamp = int(datetime.utcnow().now().timestamp() * 1000)
    msg = f'{request_method.upper()}\n{full_path}\n{timestamp}'

    if request_data:
        base64encode = base64.b64encode(json.dumps(request_data).encode()).decode()
        msg += f'\n{base64encode}'

    signed_key = hmac.new(
        bytes(secret_key, "utf-8"),
        msg=bytes(msg, "utf-8"),
        digestmod=hashlib.sha256).hexdigest()

    return signed_key, timestamp

result = create_signature(secretKey , '/oapi/v1/trade/market/history', 'GET')
sign_key = str(result[0])
timestamp = str(result[1])


import requests
import json
import time



url = "https://api.ok-ex.io/oapi/v1/trade/market/history"



payload = {}

headers = {
'Content-Type':'application/json',
'x-api-key':'2142aec0-4188-11ee-82bc-c1fe7802e12d',
'x-secret-key':'a7ac23fa-4242-591d-ad0e-81637b0aafc6',
'x-timestamp':timestamp or '',
'x-signature':sign_key or ''
}
time.sleep(1)
response = requests.request("GET", url, headers=headers, data=payload)

    




print(response.text)
print(timestamp , sign_key)
print(headers)








