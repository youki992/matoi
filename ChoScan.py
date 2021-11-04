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
from scripts import printColor,laji,zhuji
from subprocess import Popen,PIPE
from threading import Thread
from lib.core.Spider import SpiderMain
from lib.core import PortScan
from tools import awvs_add_url
from scripts import fastjson_blby
from scripts import XSS_scan
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
    console.print('''[red]
      ___                 
     /████|  ██|__   __███/   ████     ████                ████
    /██/ █   |████  █_     █  █ _       ██  █    ████|     ██  ██
    |██|      ██| |██ █(__)█|  ████| ██|       █| |██|   |██    ██
    \██| █  |██|  ██/ █_ █/   __    █   ██_|█|_ █   ███   ██    ██
      ████  ██   ██   ██     ████     ████  ████     ██    ██    
                                    [/red][yellow]code by {0}[/yellow] [blue]{1}[/blue]


'''.format(__author__, __version__))

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
        #非空取数据
        while not self._queue.empty():
            ip = self._queue.get()
            #print ip
            check_ping = Popen("ping {0} \n".format(ip), stdin=PIPE, stdout=PIPE,  shell=True)
            data = check_ping.stdout.read()
            data = data.decode("gbk")
            if 'TTL' in data:
                sys.stdout.write(ip+' is UP.\n')


def Cscan():
    pc.print_yellow_text('请输入要扫描的C段IP地址：')
    ip = input()
    index = ip.rindex(".")
    threads = []
    threads_count = 100
    q = queue.Queue()

    # 放入ip地址
    for i in range(1, 255):
        q.put(ip[:index+1] + str(i))

    for i in range(threads_count):
        threads.append(DoRun(q))

    for i in threads:
        i.start()

    for i in threads:
        i.join()


def spider():
    pc.print_yellow_text('请输入URL：')
    root = str(input()).replace('\'', '')
    threadNum = 10
    # spider
    wgd = SpiderMain(root, threadNum)
    wgd.craw()
    """
    # 用友check目录遍历
    if (YongYouCheck.YOCheck(root) == 1):
        normal_push_wechat.WeWork_Send_Msg.send_txt()
    # 用友check SQL注入
    if (YongYouCheck2.YOCheck(root) == 1):
        normal_push_wechat.WeWork_Send_Msg.send_txt()
    # 致远check
    if (ZhiYuanCheck.check(root) == 1):
        normal_push_wechat.WeWork_Send_Msg.send_txt()
    # 泛微check
    if (FanWeiCheck.check(root) == 1):
        normal_push_wechat.WeWork_Send_Msg.send_txt()
    # 亿邮check
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
    pc.print_yellow_text('请输入服务器IP地址：')
    ip = str(input())
    port = [21, 22, 23, 80, 389, 873, 1433, 1521, 2049, 2181, 3306, 3389, 4848, 5900, 6379, 7001, 8080, 8089, 9999, 11211, 27017]
    scan(ip, port)

def xray(data1):
    os.chdir("./tools")
    target = data1
    cmd = ["xray_windows_amd64.exe", "webscan", "--browser-crawler", target, "--webhook-output", "http://127.0.0.1:5000/webhook"]
    rsp = subprocess.Popen(cmd)
    output, error = rsp.communicate()
    print(output)
    os.chdir("../")

def xray_start():
    file = open("url.txt")
    for text in file.readlines():
        data1 = text.strip('\n')
        xray(data1)

def default():
    pc.print_yellow_text('无此功能，请重新运行脚本！')
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
        description="信息收集工具",
    )

    parser.add_argument("-t", dest="task",
                        help="1:纯链接式爬取  2:C段扫描  3:fastjson检测(源码配置ceye.io)  4:xss检测(配置chromedriver,参数例:'http://www.example.com?id=')",nargs='*')
    parser.add_argument("-d", dest="dir",
                        help="字典式爆破")
    parser.add_argument("-ui", dest="flask",
                        help="以交互界面式启动")
    parser.add_argument("-p", dest="port",
                        help="自定义端口扫描（ip 起始端口 终点端口）",nargs='*')
    parser.add_argument("-f", dest="finger",
                        help="CMS指纹查询（潮汐+fofa）")
    parser.add_argument("-s", dest="scan",
                        help="xray批量扫描（主目录url.txt中写入目标） awvs批量扫描（配置awvs_config.ini,主目录url.txt中写入目标）")
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
    # 解析
    if args.task is not None and args.task[0] != '3' and args.task[0] != '4':
        switch.get(args.task[0])()
    if args.task is not None and args.task[0] == '3':
        fastjson_blby.start(args.task[1])
    if args.task is not None and args.task[0] == '4':
        switch.get(args.task[0])(args.task[1])
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
    if args.scan == "awvs":
        awvs_add_url.start()
    if args.port is not None:
        PortScan.start(args.port[0],args.port[1],args.port[2])
    """
    while(1):
        pc.print_yellow_text('\n请输入数字 \n1 - 简单目录爬取  \n2 - 扫描开放端口  \n3 - 调用xray扫描（请先在url.txt中写入url，如需预警推送请先运行xray_push.py）  '
                             ' \n4 - 本地病毒扫描  \n5 - C段扫描  \n6 - 清理垃圾  \n7 - 获取主机信息  \n8 - 远程病毒扫描（请开启clamd服务） \n9 - 退出\n')
        num=str(input())
        switch.get(num,default)()
    """