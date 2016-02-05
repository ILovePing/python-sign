# -*- coding: utf-8 -*-

import requests

class youku():
    def __init__(self, cookies):
        self.s = requests.Session()
        self.url = 'http://actives.youku.com/task/signv2/qiandao?pl=web'
        self.header = {
            'Cookie':cookies,
            'Origin':'http://actives.youku.com',
            'Accept-Encoding':'gzip, deflate',
            'Host':'actives.youku.com',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            'Accept':'*/*',
            'Referer':'http://actives.youku.com/task/signv2/index',
            'X-Requested-With':'XMLHttpRequest',
            'Connection':'keep-alive',
            'Content-Length':'0',
            'DNT':'1'
        }

    def sign(self):
        res = self.s.post(self.url, headers=self.header)
        return res