#!/bin/python3

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.xxxxx.com'
CURRENT_URL = '/html/59/59872/24380385.html'

out = open('xxxxxx.txt', 'w')
s = requests.Session()

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
