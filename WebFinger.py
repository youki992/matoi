#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: DEADF1SH_CAT
@File: WebFinger.py
@Time: 2019/11/08 20:26
@About: 
'''

from socket import *
import requests
import lxml,random
from bs4 import BeautifulSoup
import sys,os,re
import sqlite3
import concurrent.futures

class WebFinger():
    def __init__(self, host, flag):
        self.host = "http://" + host
        self.finger = []
        self.re_title = re.compile(r'title="(.*)"')
        self.re_header = re.compile(r'header="(.*)"')
        self.re_body = re.compile(r'body="(.*)"')
        self.re_bracket = re.compile(r'\((.*)\)')
        if flag:
            self.threads = 50
        else:
            self.threads = 30

    requests.packages.urllib3.disable_warnings()

    def run(self):
        print("-"*20 + "Start WebFinger Matching" + "-"*20)
        if self.thread():
            print("[+] " + self.host +" use:")
            result = ""
            for i in self.finger:
                result += i + "  "
            print("[+] fofa_banner: " + result)
            """
            with open('finger.txt','w') as f:
                f.write(result)
            """
            print("-"*22 + "End WebFinger Matching" + "-"*20)

    def get_data(self):
        data = requests.get(self.host, headers=self.set_header(), timeout=3, verify=False)
        content = data.text
        title = BeautifulSoup(content, "lxml").title.text.strip()
        return data.headers, content, title.strip('\n')

    def set_header(self):
        user_agent = ['Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1) Gecko/20061010 Firefox/2.0',
                    'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0',
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1 ; x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Firefox/3.1b2pre',
                    'Opera/10.60 (Windows NT 5.1; U; zh-cn) Presto/2.6.30 Version/10.60','Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4062; en; U; ssr)',
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; ; rv:1.9.0.14) Gecko/2009082707 Firefox/3.0.14',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr; rv:1.9.2.4) Gecko/20100523 Firefox/3.6.4 ( .NET CLR 3.5.30729)',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5']
        UA = random.choice(user_agent)
        headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent':UA,
        'Upgrade-Insecure-Requests':'1','Connection':'keep-alive','Cache-Control':'max-age=0',
        'Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8',
        "Referer": "https://www.baidu.com/link?url=Ni7wOsdwUuz50m1no12V0q3QtNYXbNgXoybY9SUqoKG",
        'Cookie':"PHPSESSID=gljsd5c3ei5n813roo4878q203"}
        return headers
    
    def count(self):
        with sqlite3.connect(os.getcwd() + "./cms_finger1.db") as conn:
            cursor = conn.cursor()
            result = cursor.execute('select count(id) from `fofa`')
        for row in result:
            return row[0]

    def check(self, id):
        with sqlite3.connect(os.getcwd() + "./cms_finger1.db") as conn:
            cursor = conn.cursor()
            result = cursor.execute('select name,keys from fofa where id=\'{}\''.format(id))
            for row in result:
                return row[0], row[1]
    
    def check_key(self, key, header, body, title):
        if 'title="' in key:
            if re.findall(self.re_title, key)[0].lower() in title.lower():
                    return True
        elif 'body="' in key:
            if re.findall(self.re_body, key)[0] in body: 
                return True
        else:
            if re.findall(self.re_header, key)[0] in header: 
                return True

    def match(self, id, header, body, title):
        name, key = self.check(id)
        if '(' not in key:
            if '&&' not in key:
                if '||' not in key:
                    if self.check_key(key, header, body, title):
                        self.finger.append(name)
                elif '||' in key:
                    for re in key.split('||'):
                        if self.check_key(re, header, body, title):
                            self.finger.append(name)
                            break
            elif '&&' in key and '||' not in key:
                times = 0
                for re in key.split('&&'):
                    if self.check_key(re, header, body, title):
                        times += 1
                if times == len(key.split('&&')):
                    self.finger.append(name)
        else:
            if '&&' in re.findall(self.re_bracket, key)[0]:
                for re in key.split('||'):
                    if '&&' in re:
                        times = 0
                        for _re in key.split('&&'):
                            if self.check_key(_re, header, body, title):
                                times += 1
                        if times == len(key.split('&&')):
                            self.finger.append(name)
                            break
                    else:
                        if self.check_key(re, header, body, title):
                            self.finger.append(name)
                            break
            else:
                for re in key.split('&&'):
                    times = 0
                    if '||' in re:
                        for _re in key.split('||'):
                            if self.check_key(_re, title, body, header):
                                times += 1
                                break
                    else:
                        if self.check_key(re, title, body, header):
                            times += 1
                if times == len(key.split('&&')):
                    self.finger.append(name)
        
    def thread(self) -> bool:
        header, body, title = self.get_data()
        threadpool = concurrent.futures.ThreadPoolExecutor(max_workers = self.threads)
        futures = (threadpool.submit(self.match, sql, header, body, title) for sql in range(0, int(self.count())))
        for i in concurrent.futures.as_completed(futures):
            pass
        return True
