# -*- coding: utf-8 -*-

import requests

class acfun():
    def __init__(self, username, password):
        self.s = requests.Session()
        self.login_url = 'http://www.acfun.tv/login.aspx'
        self.sign_url = 'http://www.acfun.tv/member/checkin.aspx'
        self.username = username
        self.password = password

    def login(self):
        pload = {
            'username':self.username,
            'password':self.password
        }
        header = {
            'Pragma':'no-cache',
            'Origin':'http://www.acfun.tv',
            'Accept-Encoding':'gzip,deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept':'*/*',
            'Cache-Control':'no-cache',
            'X-Requested-With':'XMLHttpRequest',
            'Connection':'keep-alive',
            'Referer':'http://www.acfun.tv/login/'
        }
        return self.s.post(self.login_url, headers=header, data=pload)

    def sign(self):
        header = {
            'Pragma':'no-cache',
            'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive'
        }
        return self.s.get(self.sign_url)
