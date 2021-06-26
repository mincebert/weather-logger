#!/usr/bin/env python3

# temperature display client


import requests
import json
from time import sleep

import scrollphathd as sphd
import thermofont

sphd.set_font(thermofont)
#sphd.rotate(180)

while True:
    s = None

    response = None
    while True:
        try:
            response = requests.get("http://shizuka.local:8123/weather/latest")
            break
        except:
            # something went wrong - we don't care what, just wait and retry
            #sleep(20)
            pass

    if response:
        try:
            d = response.json()
            s = "%4.1f'" % d["1"]["temp"]
        except:
            pass
    else:
        print('Problem GETting!')

    sphd.clear()
    # need to handle -ve
    sphd.write_string(s or "000", brightness=0.2)
    sphd.show()

    sleep(60)
