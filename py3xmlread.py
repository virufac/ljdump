#!/usr/bin/env python3

import os, json
from pathlib import Path
from html import unescape
import xmltodict
from sys import argv, exit
from string import Template
import sys

script, journal = argv

cwd = Path.cwd()
try:
    journal = cwd.joinpath(journal)
    journal = str(journal)
except:
    print('Argument did not seem to indicate a local directory path for journal..')
    exit(1)

tojson = dict()
if cwd.joinpath(journal).exists():
    print('journal exists')
    posts = [sorted(list(f for f in os.listdir(str(journal)) if f.startswith('L-')))]
    posts = posts[0]
    comments = [sorted(list(f for f in os.listdir(str(journal)) if f.startswith('C-')))]
    comments = comments[0]

for idx, post in enumerate(posts):
    print("Starting post ", idx)
    post = journal + '/' + post

    with open(post) as fo:
        xml = fo.read()
        print(xml)

    doc = xmltodict.parse(xml)

    try:
        subject = unescape(doc['event']['subject'])
        time = unescape(doc['event']['eventtime'])
        pid =  unescape(doc['event']['itemid'])
        html = unescape(doc['event']['event'])
    except KeyError:
        print('Key Error')

    tojson[pid] = dict(data=doc, head=[subject, time], post=html)

    html_temp_file = Path.cwd().joinpath('posttemp.html')
    if html_temp_file.exists():
        with open(html_temp_file) as fo:
            html_temp = fo.read()
    else:
        html_temp.touch()

    try:
        s = Template(html_temp)
        html = s.substitute(SUBJECT=subject, TIME=time, HTML=html)
    except NameError:
        print('NameErrrir ib s.ssubstutute')
        
    fmt = f'{journal}{pid}tmp.html'
    tmp = cwd.joinpath(fmt)
    if not tmp.exists():
        with open(str(tmp), 'w') as fo:
            for line in html:
                fo.write(line)

print("Finished Journal, Saving Json")
with open('json_ljdump.json', 'w') as fo:
        json.dump(tojson, fo, indent=4)
