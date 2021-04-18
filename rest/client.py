#!/usr/bin/env python3

import requests
import json

response = requests.get('http://localhost:8000/people')
if response:
    d = response.json()
    for c in d:
        print(c, '=>', d[c])
else:
    print('Problem GETting!')

d = {
  "name": "Rob",
  "likes": "Unicorns"
}

response = requests.post('http://localhost:8000/people',
                         data=json.dumps(d),
                         headers={"Content-Type": "application/json"})
if response:
    d = response.json()
    print(d)
else:
    print("Problem POSTing!")