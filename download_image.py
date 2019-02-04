#!/usr/bin/env python

import requests

def download(url):

    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write((get_response.content))


download("http://smrafiq.com/wp-content/uploads/2016/07/25653901034_1467fc2f2f_o.jpg")
print("DOWNLOADED!")
