#!/bin/python

import sys
import re
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.uukanshu.com'

CURRENT_URL = sys.argv[1]
CURRENT_URL = CURRENT_URL.replace(BASE_URL, '')
print(CURRENT_URL)

s = requests.Session()
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
    'Cookie': '[expore from browser]',
}
r = s.get(BASE_URL + CURRENT_URL, headers=headers)
res = BeautifulSoup(r.content.decode('gb2312', 'ignore'), 'html5lib')
name = res.find(class_='shuming').find('a').string
out = open(f'{name}.txt', 'w')

while True:
    r = s.get(BASE_URL + CURRENT_URL)
    res = BeautifulSoup(r.content.decode('gb2312', 'ignore'), 'html5lib')

    title = res.find('h1', id='timu').string
    print(f'parse {title}')
    out.write(f'{title}\n')

    content = res.find(id='contentbox').find_all('p')
    for cs in content:
        for c in cs.strings:
            c = c.string
            # remove ads
            c = re.sub('UU看书.*[m|ｍ]', '', c)
            out.write(f'{c}\n')

    out.write('\n\n\n')

    CURRENT_URL = res.find(id='next').attrs['href']

    if CURRENT_URL[-4:] != 'html':
        break

out.close()
