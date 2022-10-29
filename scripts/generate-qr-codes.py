#!/usr/bin/env python

import qrcode, json, re, os
from termcolor import cprint 

outfile = "qrcode.png"
contentPath = "./docs"
filePattern = "qrcode.json"

cFilePAttern = re.compile(filePattern)
for subdir, dirs, files in os.walk(contentPath):
    for file in files:
        fileMatch = cFilePAttern.match(file)
        if fileMatch:
            cprint("Processing " + os.path.join(subdir, file), 'green')
            with open(os.path.join(subdir, file), 'r') as f:
                data = json.load(f)
            img = qrcode.make(data['url'])
            img.save(os.path.join(subdir, outfile))
            cprint("Saved file " + os.path.join(subdir, outfile), 'green')
