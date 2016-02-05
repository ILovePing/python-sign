# -*- coding: utf-8 -*-

import requests
import re

class v2ex():
    def __init__(self, username, password):
        self.s = requests.Session()
        self.username = username
        self.password = password
        self.headers = {
            'Host':'www.v2ex.com',
            'Origin':'http://www.v2ex.com',
            'Referer':'http://www.v2ex.com/signin',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        }

    def get_once(self):
        html = self.s.get('http://www.v2ex.com/signin', headers=self.headers).text
        once = re.search(r'value="(\d{5})"', html).group(1)
        return once

    def login(self):
        once = self.get_once()
        form_data = {
            'u': self.username,
            'p': self.password,
            'once': once,
            'next': '/'
        }
        res = self.s.post('http://www.v2ex.com/signin', data=form_data, headers=self.headers)
        return res

    def sign(self):
        html = self.s.get('http://www.v2ex.com/mission/daily', headers=self.headers).text
        once_code = re.search(r'signout\?once=(\d{5})', html).group(1)
        url = 'http://www.v2ex.com/mission/daily/redeem?once=' + once_code
        return self.s.get(url, headers=self.headers)