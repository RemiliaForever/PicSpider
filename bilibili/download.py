#!/bin/env python3

import os
import time
import threading

URL = 'https://www.bilibili.com/video/avxxxxxxx'
limit = 5
lock = threading.RLock()


def run(i):
    global limit
    os.system(f'youtube-dl "{URL}/index_{i}.html"')
    with lock:
        limit += 1


i = 7
while i <= 30:
    time.sleep(2)
    with lock:
        if limit > 0:
            limit -= 1
            threading.Thread(target=run, args=[i]).start()
            i += 1
        else:
            continue
