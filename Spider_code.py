# Python_Spider_study
# Maoyan top100

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import time
import json
import requests


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/68.0.3440.75 Safari/537.36'
    }
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        return response.text


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('E:/py/dandan/maoyan.txt','a')as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')


for i in range(10):
    url = 'http://maoyan.com/board/4?offset={}'.format(i*10)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
        time.sleep(1)
