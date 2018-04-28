#!/bin/python3

from bs4 import BeautifulSoup
from dbhelper import Picture

def parse(content):
    try:
        soup = BeautifulSoup(content, 'lxml')
        ul = soup.find(id='post-list-posts')
        lis = ul.find_all('li')
        l = []
        for li in lis:
            info = li.contents[0].contents[0].contents[0]['alt']
            p = Picture()
            p.rating,p.score,p.tags,p.user = split_info(info)
            p.url = 'http:' + li.contents[1]['href']
            p.size_width,p.size_height = split_size(li.contents[1].contents[1].text)
            p.preview = 'http:' + li.contents[0].contents[0].contents[0]['src']
            l.append(p)
        return l
    except Exception:
        print('parsing error!')
        return []

def split_info(info):
    infos = info.split()
    i_rating = infos.index('Rating:')
    i_score = infos.index('Score:')
    i_tags = infos.index('Tags:')
    i_user = infos.index('User:')
    return infos[i_rating+1],infos[i_score+1],' '.join(infos[i_tags+1:i_user]),infos[i_user+1]

def split_size(size):
    s = size.split()
    return s[0],s[2]
