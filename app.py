import os
import threading
from flask import request
from flask import Flask
from flask import render_template
import pymysql
import urllib.request
from bs4 import BeautifulSoup
import use_dirscan
from scripts import C_Scan
from scripts import portscan
import use_subdomain
from WebFinger import WebFinger

len1=0
len2=0
len3=0
len4=0
datalist3 = []
datalist2 = []
datalist = []

app = Flask(__name__)

# Edit Configurations -> FLASK_DEBUG √

def get_web_contents():
    global datalist
    global datalist2
    # 建立数据库连接
    db_conn = pymysql.connect(host="localhost", user="root", password="", db="craw_result", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "SELECT distinct id,title,link,zhuangtai FROM result order by id desc"
        # sql = "SELECT * FROM result where id = 1"
        print(sql)
        # 执行SQL语句
        db_conn.ping(reconnect=True)
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        for item in results:
            datalist.append(item)
            # 事物提交
        db_conn.commit()


    except Exception as err:
        print("sql语句执行错误", err)
        db_conn.rollback()

        db_conn.close()
    """
    for item in datalist:
        #print(item[2])
        page = urllib.request.urlopen(item[2])
        contents = page.read().decode("utf-8", "ignore")
        datalist2.append(str(contents))
    global datalist3
    """
    datalist3 = zip(datalist, datalist2)

# 主页
@app.route('/')
def index():

    global datalist3
    if not datalist3:
        threads = threading.Thread(target=get_web_contents())
        threads.start()
        #print(datalist3)
    return render_template('index.html', len11 = len1+len2+len3+len4)


# 首页
@app.route('/index')
def home():
    """
    global datalist3
    if not datalist3:
        threads = threading.Thread(target=get_web_contents())
        threads.start()
        print(datalist3)


    for item in datalist:
        #print(item[2])
        page = urllib.request.urlopen(item[2])
        contents = page.read().decode("utf-8","ignore")
        datalist2.append(str(contents))
    # 获得了整个网页的内容也就是源代码
    #print(str(contents))
    """
    # return render_template('index.html')
    return index()


# 帖子详情
@app.route('/title')
def title():
    global datalist2
    #print(datalist2)
    """
        datalist = []
        datalist2 = []
        # 建立数据库连接
        db_conn = pymysql.connect(host="localhost", user="root", password="", db="craw_result", charset="utf8")

        # 创建游标对象
        cur = db_conn.cursor()
        # 执行sql语句
        try:
            # 执行sql语句
            sql = "SELECT distinct id,title,link,zhuangtai FROM result order by id desc"
            # sql = "SELECT * FROM result where id = 1"
            print(sql)
            # 执行SQL语句
            db_conn.ping(reconnect=True)
            cur.execute(sql)
            # 获取所有记录列表
            results = cur.fetchall()
            for item in results:
                datalist.append(item)
                # 事物提交
            db_conn.commit()


        except Exception as err:
            print("sql语句执行错误", err)
            db_conn.rollback()

            db_conn.close()
        for item in datalist:
            #print(item[2])
            page = urllib.request.urlopen(item[2])
            contents = page.read().decode("utf-8","ignore")
            datalist2.append(str(contents))
            # 获得了整个网页的内容也就是源代码
            #print(str(contents))
            #print(datalist3)
            datalist3 = zip(datalist, datalist2)
    """
    global datalist3
    datalist3 = []
    datalist3 = zip(datalist, datalist2)
    return render_template('title.html',renting=datalist3)


# 团队
@app.route('/person')
def person():
    return render_template('person.html')


# 词云
@app.route('/word')
def count():
    return render_template('word.html')


# 详细信息
@app.route('/info')
def info():
    # 建立数据库连接
    db_conn = pymysql.connect(host="localhost", user="root", password="", db="craw_result", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor();
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "SELECT count(distinct id,title,link) FROM result ORDER BY id desc"
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
    return render_template('info.html',len1 = int(results[0][0]))

@app.route('/list')
def list():
    # 建立数据库连接
    db_conn = pymysql.connect(host="localhost", user="root", password="", db="craw_result", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    uid = 1
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "SELECT count(distinct title,link) FROM result"
        # sql = "SELECT * FROM result where id = 1"
        print(sql)
        # 执行SQL语句
        db_conn.ping(reconnect=True)
        cur.execute(sql)
        # 获取所有记录列表
        uid = cur.fetchall()

    except Exception as err:
        print("sql语句执行错误", err)
        db_conn.rollback()

    db_conn.close()

    db_conn = pymysql.connect(host="localhost", user="root", password="", db="port_scan", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "select count(distinct ip,port) from result"
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

    db_conn = pymysql.connect(host="localhost", user="root", password="", db="C_scan", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "select count(distinct ip,C_ip) from result"
        # sql = "SELECT * FROM result where id = 1"
        print(sql)
        # 执行SQL语句
        db_conn.ping(reconnect=True)
        cur.execute(sql)
        # 获取所有记录列表
        results2 = cur.fetchall()

        # 事物提交
        db_conn.commit()

    except Exception as err:
        print("sql语句执行错误", err)
        db_conn.rollback()

    db_conn.close()

    db_conn = pymysql.connect(host="localhost", user="root", password="", db="subdomain", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "select count(distinct ips,subdomain) from result"
        # sql = "SELECT * FROM result where id = 1"
        print(sql)
        # 执行SQL语句
        db_conn.ping(reconnect=True)
        cur.execute(sql)
        # 获取所有记录列表
        results3 = cur.fetchall()

        # 事物提交
        db_conn.commit()

    except Exception as err:
        print("sql语句执行错误", err)
        db_conn.rollback()

    db_conn.close()
    global datalist3
    if not datalist3:
        threads = threading.Thread(target=get_web_contents())
        threads.start()
        print(datalist3)
    global len1
    len1 = int(uid[0][0])
    global len2
    len2 = int(results[0][0])
    global len3
    len3 = int(results2[0][0])
    global len4
    len4 = int(results3[0][0])
    return render_template('list.html',len1 = len1 ,len2 = int(results[0][0]) ,len3 = int(results2[0][0]) , len4 = int(results3[0][0]))

@app.route('/list2')
def list2():
    datalist = []
    # 建立数据库连接
    db_conn = pymysql.connect(host="localhost", user="root", password="", db="port_scan", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "SELECT distinct id,ip,port FROM result ORDER BY id desc"
        # sql = "SELECT * FROM result where id = 1"
        print(sql)
        # 执行SQL语句
        db_conn.ping(reconnect=True)
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        for item in results:
            datalist.append(item)
        # 事物提交
        db_conn.commit()

    except Exception as err:
        print("sql语句执行错误", err)
        db_conn.rollback()

    db_conn.close()
    return render_template('list2.html', renting=datalist)

@app.route('/C_scan')
def C_scan():
    datalist = []
    # 建立数据库连接
    db_conn = pymysql.connect(host="localhost", user="root", password="", db="C_scan", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "SELECT distinct id,ip,C_ip,response FROM result order by id desc"
        # sql = "SELECT * FROM result where id = 1"
        print(sql)
        # 执行SQL语句
        db_conn.ping(reconnect=True)
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        for item in results:
            datalist.append(item)
        # 事物提交
        db_conn.commit()

    except Exception as err:
        print("sql语句执行错误", err)
        db_conn.rollback()

    db_conn.close()
    return render_template('C_scan.html', renting=datalist)

@app.route('/input1',methods = ['POST'])
def input1():
    http = request.form.get('http')
    threads = [threading.Thread(target=use_dirscan.start, args=(http,))]
    for t in threads:
        # 启动线程
        t.start()

    #use_dirscan.start(http)
    return render_template('index.html', len11=len1+len2+len3)

@app.route('/input2',methods = ['POST'])
def input2():
    ip = request.form.get('ip')
    threads = [threading.Thread(target=C_Scan.main, args=(ip,)),
               threading.Thread(target=portscan.main, args=[ip, 10])]
    for t in threads:
        # 启动线程
        t.start()

    #C_Scan.main(ip)
    #portscan.main(ip, 10)
    return render_template('index.html', len11=len1+len2+len3)

@app.route('/saomiao')
def saomiao():
    return render_template('saomiao.html')

@app.route('/subdomain')
def domain():
    datalist = []
    # 建立数据库连接
    db_conn = pymysql.connect(host="localhost", user="root", password="", db="subdomain", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "SELECT distinct id,subdomain,ips FROM result order by id desc"
        # sql = "SELECT * FROM result where id = 1"
        print(sql)
        # 执行SQL语句
        db_conn.ping(reconnect=True)
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        for item in results:
            datalist.append(item)
        # 事物提交
        db_conn.commit()

    except Exception as err:
        print("sql语句执行错误", err)
        db_conn.rollback()

    db_conn.close()
    return render_template('subdomain.html', renting=datalist)

@app.route('/input3',methods = ['POST'])
def domain_scan():
    ip = request.form.get('domain')
    threads = [threading.Thread(target=use_subdomain.start(ip))]
    # 启动线程
    for t in threads:
        t.start()
    # C_Scan.main(ip)
    # portscan.main(ip, 10)
    return render_template('index.html', renting=datalist)

@app.route('/finger')
def finger():
    return render_template('finger.html')

@app.route('/input4',methods = ['POST'])
def finger_scan():
    ip = request.form.get('url')
    web = WebFinger(ip, 0)
    web.run()
    """
    with open('finger.txt', 'r') as f:
        finger = f.read()
    """
    return render_template('index.html', renting=finger)

if __name__ == '__main__':
    app.run(threaded=True,port=6000)