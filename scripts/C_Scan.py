import subprocess as p
import time
import threading
from queue import Queue

import pymysql
import requests
from bs4 import BeautifulSoup

before_ip = ''

def check_ip(ip):
    w=p.Popen('ping -n 2 '+ip,shell=True,stdout=p.PIPE,stderr=p.PIPE,encoding='gbk')
    result=w.stdout.read()
    # print(result)
    if 'TTL' in result:
        try:
            t_url = 'http://'+str(ip)
            res = requests.get(t_url)
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text, 'html.parser')
            print(soup.title.text)
            print(ip, 'is Up')
            db_conn = pymysql.connect(host="localhost", user="root", password="", db="C_scan", charset="utf8")

            # 创建游标对象
            cur = db_conn.cursor();
            # 执行sql语句
            try:
                # 执行sql语句
                sql = "insert into result values('%s','%s','%s','%s')" % (str(time.time()),before_ip,ip,soup.title.text)
                # sql = "SELECT * FROM result where id = 1"
                print(sql)
                # 执行SQL语句
                db_conn.ping(reconnect=True)
                cur.execute(sql)
                # 获取所有记录列表
                results = cur.fetchall()

                # 事物提交
                db_conn.commit()

            except Exception as err:
                print("sql语句执行错误", err)
                db_conn.rollback()

            db_conn.close()
        except:
            print(ip,'is Up')
def main(C_ip):
    q=Queue()
    threads=[]
    threads_count=255
    global before_ip
    before_ip = C_ip
    addr = before_ip.strip().split('.')  # 切割IP地址为一个列表
    ips =''
    for i in range(3):
        ips+=addr[i]+'.'
    #ips = '183.246.196.'
    print('ips:'+ips)
    for i in range(1,255):
        q.put(ips+str(i))
        # print(q.get())
    for i in range(threads_count):
        t=threading.Thread(target=check_ip,args=(q.get(),))
        t.start()
        threads.append(t)
        time.sleep(0.2)
    for i in threads:
        i.join()
    print('all done')
"""
if __name__ == '__main__':
  main()
"""