#!/usr/bin/env python3

import os, requests
fields = ['name', 'weight', 'description', 'image_name']

os.chdir('./supplier-data/descriptions')
for txt in os.listdir():
    if not txt.endswith('.txt'):
        continue
    data=None
    with open(txt, 'r') as f:
        data=f.readlines()
    data[1] = int(data[1].split(' ')[0])
    img_name = txt.replace('.txt', '.jpeg')
    print(img_name)
    d = {fields[3]:img_name}
    for i in range(len(data)):
        d[fields[i]]=data[i]
#    print(d)
    r=requests.post('http://localhost/fruits/', data=d)
    print(r)
