#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
os.chdir('./supplier-data/images')

files=[]
for f in os.listdir():
    fsplit = f.split('.')
    if len(fsplit)==1 or fsplit[1]!='jpeg':
        continue
    files.append(f)

for f in files:
    with open(f, 'rb') as d:
        print(f)
        r = requests.post(url, files={'file': d})
        print(r)
