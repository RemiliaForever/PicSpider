#!/bin/python3

from dbhelper import *
from parser import parse
import grequests
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import sys

requests_session = requests.Session()
retries = Retry(total=10, backoff_factor=0.1, status_forcelist=[500,502,503,504])
requests_session.mount('http://', HTTPAdapter(max_retries=retries))
requests_session.mount('https://', HTTPAdapter(max_retries=retries))

session = DBSession()

start_page = int(sys.argv[1])
end_page = int(sys.argv[2])

urls = []
for page in range(start_page, end_page+1):
    urls.append(grequests.get('http://konachan.net/post?page={0}'.format(page), session=requests_session))

print('\nDownloading page : {0}\n'.format(len(urls)))
pics = []
k = 0
for i in grequests.imap(urls, size=10):
    k += 1
    print('({0}/{1})\tparsing page '.format(k, end_page-start_page+1) + i.url + '\t{0}'.format(i.status_code))
    pics.extend(parse(i.content))


print('\nDownloading preview : {0}\n'.format(len(pics)))

urls.clear()
picmap = {}
for pic in pics:
    urls.append(grequests.get(pic.preview, session=requests_session))
    picmap.update({pic.preview:pic})

k = 0
session.autocommit = True
for i in grequests.imap(urls, size=10):
    k += 1
    print('({0}/{1})\tsaving...'.format(k, len(urls)))
    p = picmap.get(i.url)
    p.preview = i.content
    session.add(p)
session.commit()
session.flush()
session.close()
