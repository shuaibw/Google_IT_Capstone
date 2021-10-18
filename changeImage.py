#!/usr/bin/env python3
from PIL import Image
import os

os.chdir('./supplier-data/images')
files = os.listdir()

for f in files:
    suffix = f.split('.')
    if len(suffix)==1 or suffix[1]!='tiff':
        continue
    im = Image.open(f)
    im.resize((600, 400)).convert('RGB').save(suffix[0]+'.jpeg', format = 'JPEG')
    im.close()

