#!/usr/bin/env python3

import requests
import json
import time

import scrollphathd as sphd
import thermofont

sphd.set_font(thermofont)
sphd.rotate(180)

while True:
    response = requests.get("http://shizuka.local:8123/weather/latest")
    if response:
        d = response.json()
        for s in d:
            print(s, "=>", d[s])
    else:
        print('Problem GETting!')

    sphd.clear()
    # need to handle -ve
    sphd.write_string("%4.1f'" % d["1"]["temp"], brightness=0.3)
    sphd.show()

    time.sleep(60)
