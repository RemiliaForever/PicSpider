#!/bin/python3

import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.xxxxx.com'

CURRENT_URL = sys.argv[1]
CURRENT_URL = CURRENT_URL.replace(BASE_URL, '')
print(CURRENT_URL)

s = requests.Session()

r = s.get(BASE_URL + CURRENT_URL)
res = BeautifulSoup(r.content)
name = res.find(id='amain').find('dl').find('dt').findAll('a')[-1].string
out = open(f'{name}.txt', 'w')

while True:
    r = s.get(BASE_URL + CURRENT_URL)
    res = BeautifulSoup(r.content)

    title = res.find('h1').string
    print(f'parse {title}')
    out.write(f'{title}\n')

    content = res.find(id='contents').strings
    for c in content:
        out.write(f'{c}\n')

    out.write('\n\n\n')

    CURRENT_URL = res.find(id='footlink').find_all('a')[2].attrs['href']

    if CURRENT_URL[-4:] != 'html':
        break

out.close()
