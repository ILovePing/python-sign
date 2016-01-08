# coding: utf-8

import requests
import re

class v2ex():
    def __init__(self):
        self.s = requests.Session()
        self.headers = {
            'Host':'www.v2ex.com',
            'Origin':'http://www.v2ex.com',
            'Referer':'http://www.v2ex.com/signin',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        }

    def get_once(self):
        html = self.s.get('http://www.v2ex.com/signin', headers=self.headers).content
        once = re.search(r'value="(\d{5})"', html).group(1)
        return once

    def login(self, username, password, once):
        form_data = {
            'u': username,
            'p': password,
            'once': once,
            'next': '/'
        }
        res = self.s.post('http://www.v2ex.com/signin', data=form_data, headers=self.headers)
        return res

    def sign(self):
        html = self.s.get('http://www.v2ex.com/mission/daily', headers=self.headers).content
        once_code = re.search(r'signout\?once=(\d{5})', html).group(1)
        url = 'http://www.v2ex.com/mission/daily/redeem?once=' + once_code
        return self.s.get(url, headers=self.headers)

if __name__ == '__main__':
    v2ex = v2ex()
    once = v2ex.get_once()
    v2ex.login('用户名', '密码', once)
    v2ex.sign()