#!/usr/bin/env python

import requests
subdomains = []
def request(url):
    try:
        get_response = requests.get("http://"+ url)
        return get_response
    except:
        print("final")
target_url = "www.ajwapaste.com.pk"


response = request(target_url)
if response:
    print("[+] Discoverd subdomain --> " + response.url)
    subdomains.append(response.url)
