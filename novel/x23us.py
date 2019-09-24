#!/bin/python3

import sys
import requests
import re
from bs4 import BeautifulSoup

BASE_URL = 'https://www.x23us.com'

CURRENT_URL = sys.argv[1]
CURRENT_URL = CURRENT_URL.replace(BASE_URL, '')
print(CURRENT_URL)

s = requests.Session()

r = s.get(BASE_URL + CURRENT_URL)
res = BeautifulSoup(r.content, 'html5lib')
name = res.find(id='amain').find('dl').find('dt').findAll('a')[-1].string
out = open(f'{name}.txt', 'w')

last = ''
while True:
    r = s.get(BASE_URL + CURRENT_URL)
    res = BeautifulSoup(r.content, 'html5lib')

    title = res.find('h1').string
    print(f'parse {title}')
    NEW_URL = res.find(id='footlink').find_all('a')[2].attrs['href']
    if CURRENT_URL == NEW_URL:
        print('got last')
        break
    CURRENT_URL = NEW_URL

    if title == last:
        print('duplicate, skip')
        continue
    last = title

    out.write(f'{title}\n')

    content = res.find(id='contents').strings
    for c in content:
        c = re.sub('顶点小说.*更新最快', '', c)
        out.write(f'{c}\n')

    out.write('\n\n\n')

    if CURRENT_URL[-4:] != 'html':
        break

out.close()
