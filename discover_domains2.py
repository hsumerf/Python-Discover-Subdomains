#!/usr/bin/env python

import requests
import sys
def request(url):
    try:
        get_response = requests.get("http://"+ url)
        return get_response
    except Exception:
        pass

subdomains = []
target_url = "ajwapaste.com.pk/"
with open("subdomains-wordlist.txt","r") as wordlist_file:
    send_packets_count = 0
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        send_packets_count = send_packets_count + 1
        # \r means always start from the start of the line
        print("\r[+] Line No. "+str(send_packets_count)),
        sys.stdout.flush()
        if response:
            print("[+] Discoverd subdomain --> " + response.url)
            subdomains.append(response.url)

    print("[+] Finish list!")
    print(subdomains)
