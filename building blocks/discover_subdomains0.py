#!/usr/bin/env python

import requests

url = "ajwapaste.com.pk"
get_response = requests.get("http://"+ url)

print(get_response)
