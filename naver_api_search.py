#!/usr/bin/python3

import requests
import pprint

client_id = "yourid"
client_secret = "yoursecretkey"

header = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}

#url = "https://openapi.naver.com/v1/search/blog" blog
url = "https://openapi.naver.com/v1/search/news"

param = {"query":"코로나",'display':10}

r = requests.get(url, params=param, headers=header)

result = r.json() # json

pprint.pprint(result)
