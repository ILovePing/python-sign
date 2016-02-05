# -*- coding: utf-8 -*-

import requests

class neteasemusic():
    def __init__(self, cookie):
        self.s = requests.Session()
        self.url = 'http://music.163.com/api/point/dailyTask?type=1&csrf_token=123'
        self.header = {
            'Pragma':'no-cache',
            'DNT':'1',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'en,zh-CN;q=0.8,zh;q=0.6',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.30 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded',
            'Accept':'*/*',
            'Cache-Control':'no-cache',
            'Referer':'http://music.163.com/discover',
            'Cookie':cookie,
            'Connection':'keep-alive',
        }

    def sign(self):
        return self.s.get(self.url, headers=self.header)