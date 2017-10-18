#!/usr/bin/python3

import requests
import json

url = "https://api.chucknorris.io/jokes/random"
r = requests.get(url=url)
#print(r)
json_data = (r.json())
#print(json_data)
response = "*Chuck Norris says:* \n"
response += json_data['value']

print(response)
