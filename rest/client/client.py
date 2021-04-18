#!/usr/bin/env python3

import requests
import json

response = requests.get('http://shizuka.local:8123/weather/latest')
if response:
    d = response.json()
    for s in d:
        print(s, "=>", d[s])
else:
    print('Problem GETting!')
