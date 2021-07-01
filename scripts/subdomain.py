#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import dns.resolver
import threading
import queue
import optparse
import sys

import pymysql

queue = queue.Queue()
lock = threading.Lock()

class GetSubDomain(threading.Thread):
    """docstring for SubDomain"""
    def __init__(self, target,queue,outfile):
        threading.Thread.__init__(self)
        self.target = target
        self.queue = queue
        self.rsv = dns.resolver.Resolver()
        outfile = target + '.txt' if not outfile else outfile
        self.f = open('./output/'+outfile,'a+')
        self.ip_list = []

    def _scan(self):
        while not self.queue.empty():
            self.ip_list = []
            ips = None
            sub_domain = self.queue.get() + '.' + self.target
            for _ in range(3):
                try:
                    answers = self.rsv.query(sub_domain)
                    if answers:
                        for answer in answers:
                            if answer.address not in self.ip_list:
                                self.ip_list.append(answer.address)
                except dns.resolver.NoNameservers as e:
                    break
                except Exception as e:
                    pass
            if len(self.ip_list)>0:
                ips = ','.join(self.ip_list)
                db_conn = pymysql.connect(host="localhost", user="root", password="", db="subdomain",
                                          charset="utf8")

                # 创建游标对象
                cur = db_conn.cursor();

                # 执行sql语句
                try:
                    # 执行sql语句
                    sql = "insert into result values('%s','%s','%s')" % (time.time(), sub_domain, ips)
                    # sql = "SELECT * FROM result where id = 1"
                    print(sql)
                    # 执行SQL语句
                    db_conn.ping(reconnect=True)
                    cur.execute(sql)

                    # 事物提交
                    db_conn.commit()

                except Exception as err:
                    print("sql语句执行错误", err)
                    db_conn.rollback()

                db_conn.close()
                msg = sub_domain.ljust(30) + ips + '\n'
                lock.acquire()
                print(msg)
                self.f.write(msg)
                lock.release()
            self.queue.task_done()

    def run(self):
        self._scan()

def get_target(domain_list):
    targets = []
    for line in open(domain_list,'r'):
        if line:
            targets.append(line.strip())
    return targets

def get_sub_queue(sub_file): #得到所有子域名的queue
    for line in open(sub_file,'r'):
        if line:
            queue.put(line.strip())

def main():
    parser = optparse.OptionParser()
    parser.add_option('-u', '--url', dest='url',
        type='string', help='Get a single top-level domain names.')
    parser.add_option('-l', '--list', dest='domain_list',
        type='string', help='Top-level domain name list.')
    parser.add_option('-f', '--file', dest='sub_file', default='./dic/sub.txt',
        type='string', help='Dict file used to brute sub names')
    parser.add_option('-t', '--threads', dest='threads_num', default=60,
        type='int', help='Number of threads. default = 60')
    parser.add_option('-o', '--outfile', dest='outfile', default=None,
        type='string', help='Output file name. default is {target}.txt')

    (options, args) = parser.parse_args()
    if options.url:
        urls = [options.url]
    elif options.domain_list:
        urls = get_target(options.domain_list)
    else:
        parser.print_help()
        print("Example: ")
        print("\tpython getsub.py -u baidu.com")
        print("\tpython getsub.py -l domain.txt -f sub.txt -t 50")
        sys.exit(0)

    for url in urls:
        get_sub_queue(options.sub_file)
        for x in range(1,options.threads_num+1):
            t = GetSubDomain(url,queue,options.outfile)
            t.setDaemon(True)
            t.start()
        queue.join()

if __name__ == '__main__':
    main()