#!/usr/bin/python3

import requests
import pprint

client_id = "yourid"
client_secret = "yoursecretkey"

header = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}

url = "https://openapi.naver.com/v1/papago/n2mt"

param = {"source":"en", "target":"ko","text":"welcome"}

r = requests.post(url, data=param, headers=header)

result = r.json()

pprint.pprint(result['message'])
