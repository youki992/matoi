#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import time
import pyclamd
import threading
import queue
import os
import subprocess
import socket
import argparse
from scripts import printColor
from subprocess import Popen,PIPE
from threading import Thread
from lib.core.Spider import SpiderMain
from lib.core import PortScan
from scripts import fastjson_blby
from scripts import XSS_scan
from scripts import your_poc
from scripts import YongYouCheck
from scripts import YongYouCheck2
from scripts import ZhiYuanCheck
from scripts import FanWeiCheck
from scripts import YiYouCheck
from lib.core import normal_push_wechat
from rich.console import Console
import use_dirscan
import use_app
import use_tide
from WebFinger import WebFinger


__author__ = 'chobits'
__date__ = '2021/08/25'
__version__ = 'v0.3'

console = Console()

def banner():
    show = r'''

       .__                                       
  ____ |  |__   ____  ______ ____ _____    ____  
_/ ___\|  |  \ /  _ \/  ___// ___\\__  \  /    \ 
\  \___|   Y  (  <_> )___ \\  \___ / __ \|   |  \
 \___  >___|  /\____/____  >\___  >____  /___|  /
     \/     \/           \/     \/     \/     \/ 

    					coded by chobits v0.4
    	'''
    print(show + '\n')

class Scan(Thread):
    def __init__(self, IP, scan_type, file):
        Thread.__init__(self)
        self.IP = IP
        self.scan_type = scan_type
        self.file = file
        self.connstr = ""
        self.scanresult = ""

    def run(self):
        try:
            cd = pyclamd.ClamdNetworkSocket(self.IP, 3310)
            if cd.ping():
                self.connstr = self.IP + " connection [OK]"
                cd.reload()
                if self.scan_type == "contscan_file":
                    self.scanresult = "{0}\n.".format(cd.contscan_file(self.file))
                elif self.scan_type == "multiscan_file":
                    self.scanresult = "{0}\n.".format(cd.multiscan_file(self.file))
                elif self.scan_type == "scan_file":
                    self.scanresult = "{0}\n.".format(cd.scan_file(self.file))
                time.sleep(1)
            else:
                self.connstr = self.IP + " ping error, exit"
                return
        except Exception as e:
            self.connstr = self.IP + " " + str(e)


class DoRun(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        #???????????????
        while not self._queue.empty():
            ip = self._queue.get()
            #print ip
            check_ping = Popen("ping {0} \n".format(ip), stdin=PIPE, stdout=PIPE,  shell=True)
            data = check_ping.stdout.read()
            data = data.decode("gbk")
            if 'TTL' in data:
                sys.stdout.write(ip+' is UP.\n')


def Cscan():
    pc.print_yellow_text('?????????????????????C???IP?????????')
    ip = input()
    index = ip.rindex(".")
    threads = []
    threads_count = 100
    q = queue.Queue()

    # ??????ip??????
    for i in range(1, 255):
        q.put(ip[:index+1] + str(i))

    for i in range(threads_count):
        threads.append(DoRun(q))

    for i in threads:
        i.start()

    for i in threads:
        i.join()


def spider():
    pc.print_yellow_text('?????????URL???')
    root = str(input()).replace('\'', '')
    threadNum = 10
    # spider
    wgd = SpiderMain(root, threadNum)
    wgd.craw()
    """
    # ??????check????????????
    if (YongYouCheck.YOCheck(root) == 1):
        normal_push_wechat.WeWork_Send_Msg.send_txt()
    # ??????check SQL??????
    if (YongYouCheck2.YOCheck(root) == 1):
        normal_push_wechat.WeWork_Send_Msg.send_txt()
    # ??????check
    if (ZhiYuanCheck.check(root) == 1):
        normal_push_wechat.WeWork_Send_Msg.send_txt()
    # ??????check
    if (FanWeiCheck.check(root) == 1):
        normal_push_wechat.WeWork_Send_Msg.send_txt()
    # ??????check
    if (YiYouCheck.check(root) == 1):
        normal_push_wechat.WeWork_Send_Msg.send_txt()
    """

def portscan(ip,port):
    #portscan
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False

def scan(ip, port):
    for x in port:
        r = portscan(ip, x)
        if r:
            pc.print_green_text('%s:%s is open' % (ip, x))
        else:
            print('%s:%s is close' % (ip, x))

def scan_start():
    pc.print_yellow_text('??????????????????IP?????????')
    ip = str(input())
    port = [21, 22, 23, 80, 389, 873, 1433, 1521, 2049, 2181, 3306, 3389, 4848, 5900, 6379, 7001, 8080, 8089, 9999, 11211, 27017]
    scan(ip, port)

def xray(data1):
    target = data1
    cmd = ["./tools/xray_windows_amd64.exe", "webscan", "--browser-crawler", target, "--webhook-output", "http://127.0.0.1:5000/webhook"]
    rsp = subprocess.Popen(cmd)
    output, error = rsp.communicate()
    print(output)

def xray_start():
    file = open("url.txt")
    for text in file.readlines():
        data1 = text.strip('\n')
        xray(data1)

def default():
    pc.print_yellow_text('???????????????????????????????????????')
    quit()

def exit_r():
    exit()
switch = {'1' : spider,
          '2' : Cscan,
          """
          '3' : xray_start,
          '4' : SecurityMana,
          """
          '3' : fastjson_blby.start,
          '4' : XSS_scan.check_xss,
          }

if __name__ == '__main__':
    banner()
    pc = printColor.Colors()
    parser = argparse.ArgumentParser(
        usage='\npython choscan.py [optional arguments]',
        description="??????????????????",
    )

    parser.add_argument("-t", dest="task",
                        help="Example:-t number  1:??????????????????  2:C?????????  3:fastjson??????(????????????ceye.io)  4:xss??????(??????chromedriver,?????????:'http://www.example.com?id='  5:?????????POC??????)",nargs='*')
    parser.add_argument("-d", dest="dir",
                        help="???????????????;Example:-d url")
    parser.add_argument("-ui", dest="flask",
                        help="????????????????????????;Example:-ui flask")
    parser.add_argument("-p", dest="port",
                        help="?????????????????????;Example:-p ip portStart portEnd",nargs='*')
    parser.add_argument("-f", dest="finger",
                        help="CMS????????????;Example:-f url")
    parser.add_argument("-s", dest="scan",
                        help="xray????????????????????????url.txt??????????????????;Example:-f xray")
    """
    parser.add_argument("-w", dest="wordlist", type=str, default="./wordlist.txt",
                        help="Customize wordlist (default wordlist.txt) or a single path")
    parser.add_argument("-t", dest="threads", type=int, default=20,
                        help="Set thread (default 20)")
    parser.add_argument("-v", dest="verbose", action="store_true",
                        help="show verbose")
    """
    args = parser.parse_args()
    #print(args.task)
    if args.task is None and args.finger is None and args.dir is None and args.flask is None and args.scan is None and args.port is None:
        console.print("[[x]] python3 choscan.py -h")
        exit(0)
    # ??????
    if args.task is not None and args.task[0] != '3' and args.task[0] != '4' and args.task[0] != '5':
        switch.get(args.task[0])()
    if args.task is not None and args.task[0] == '3':
        fastjson_blby.start(args.task[1])
    if args.task is not None and args.task[0] == '4':
        switch.get(args.task[0])(args.task[1])
    if args.task is not None and args.task[0] == '5':
        your_poc.start()
    if args.dir is not None:
        use_dirscan.start(args.dir)
    if args.flask == "flask":
        use_app.start()
    if args.finger is not None:
        use_tide.start(args.finger)
        web = WebFinger(args.finger.replace('https://','').replace('http://',''), 0)
        web.run()
    if args.scan == "xray":
        xray_start()
    if args.port is not None:
        PortScan.start(args.port[0],args.port[1],args.port[2])
    """
    while(1):
        pc.print_yellow_text('\n??????????????? \n1 - ??????????????????  \n2 - ??????????????????  \n3 - ??????xray??????????????????url.txt?????????url?????????????????????????????????xray_push.py???  '
                             ' \n4 - ??????????????????  \n5 - C?????????  \n6 - ????????????  \n7 - ??????????????????  \n8 - ??????????????????????????????clamd????????? \n9 - ??????\n')
        num=str(input())
        switch.get(num,default)()
    """