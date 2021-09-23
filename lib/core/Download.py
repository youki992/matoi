#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


class Downloader(object):
    def get(self, url):
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None
        _str = r.text
        return _str

    def post(self, url, data):
        r = requests.post(url, data)
        _str = r.text
        return _str

    def download(self, url, htmls):
        if url is None:
            return None
        _str = {}
        _str["url"] = url
        try:
            r = requests.get(url, timeout=10)
            if r.status_code != 200:
                return None
            _str["html"] = r.text
        except Exception as e:
            return None
        htmls.append(_str)
