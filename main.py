# -*- coding: utf-8 -*-

from sign_v2ex import v2ex
from sign_youku import youku
from sign_neteasemusic import neteasemusic
from sign_acfun import acfun

if __name__ == '__main__':
    # V2EX
    v2ex = v2ex('', '')
    v2ex.login()
    v2ex.sign()
    # 优酷
    youku = youku('')
    youku.sign()
    # 网易云音乐
    neteasemusic = neteasemusic('')
    neteasemusic.sign()
    # actun
    acfun = acfun('', '')
    acfun.login()
    acfun.sign()