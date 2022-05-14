import os
import subprocess
import threading
from concurrent.futures.thread import ThreadPoolExecutor
import re
import requests
from flask import request
from flask import Flask
from flask import render_template
import pymysql
import time
import urllib.request
from bs4 import BeautifulSoup
import use_dirscan
import use_tide
from scripts import C_Scan
from scripts import portscan
import use_subdomain
import eventlet
from WebFinger import WebFinger
from flask import make_response
from flask import send_file
import smtplib
from email.mime.text import MIMEText

len1=0
len2=0
len3=0
len4=0
datalist3 = []
datalist2 = []
datalist = []
flag=0
file_name=''

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

def xray(target):

    global flag
    global file_name
    if flag == 1:
        print('已开始扫描')
    else:
        flag = 1
        # 建立数据库连接
        db_conn = pymysql.connect(host="localhost", user="root", password="", db="xray", charset="utf8")
        # 创建游标对象
        cur = db_conn.cursor()
        # 执行sql语句
        try:
            # 执行sql语句
            sql = "insert into name values('%s','%s')" % (str(time.time()),target)
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
        try:
            # 执行sql语句
            sql = "SELECT distinct id,ip FROM name order by id desc limit 0,1"
            print(sql)
            # 执行SQL语句
            db_conn.ping(reconnect=True)
            cur.execute(sql)
            # 获取所有记录列表
            results = cur.fetchall()
            file_name = str(results[0][0]) + '.html'
            print(file_name)
            # 事物提交
            db_conn.commit()

        except Exception as err:
            print("sql语句执行错误", err)
            db_conn.rollback()

        db_conn.close()
        cmd = ["./tools/xray_windows_amd64.exe", "webscan", "--browser-crawler", target, "--webhook-output", "http://127.0.0.1:5000/webhook", "--html-output", file_name]
        rsp = subprocess.Popen(cmd)
        flag = 0


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

    datalist = []
    datalist2 = []

    def action(datalist):
        for item in datalist:
            try:
                r = requests.get(item[2], timeout=0.1)
                print(r.headers)
                datalist2.append(r.headers)
            except:
                print('超时')
                datalist2.append('请求超时')


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

    # 创建一个包含2条线程的线程池
    pool = ThreadPoolExecutor(max_workers=20)
    # 向线程池提交一个task, 50会作为action()函数的参数
    future1 = pool.submit(action, datalist)
    # 判断future1代表的任务是否结束
    time.sleep(3)
    # 关闭线程池
    pool.shutdown()
    global datalist3
    datalist3 = []
    datalist3 = zip(datalist, datalist2)

    return render_template('title.html',renting=datalist3)


# 团队
@app.route('/subdomain_list')
def subdomain_list():
    return render_template('subdomain_list.html')


@app.route('/word')
def count():
    return render_template('word.html')

@app.route('/setting')
def setting():
    return render_template('setting.html')

# 详细信息
@app.route('/info')
def info():
    # 建立数据库连接
    db_conn = pymysql.connect(host="localhost", user="root", password="", db="craw_result", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
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
    print(datalist)
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

@app.route('/attack')
def attack():
    db_conn = pymysql.connect(host="localhost", user="root", password="", db="vul", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "select count(*) from vul where id in (select max(id) from vul group by time) order by name desc,id desc"
        # sql = "SELECT * FROM result where id = 1"
        print(sql)
        # 执行SQL语句
        db_conn.ping(reconnect=True)
        cur.execute(sql)
        # 获取所有记录列表
        attack_results = cur.fetchall()
        # 事物提交
        db_conn.commit()

    except Exception as err:
        print("sql语句执行错误", err)
        db_conn.rollback()

    db_conn.close()
    return render_template('attack.html',len=int(attack_results[0][0]))

@app.route('/input4',methods = ['POST'])
def finger_scan():
    url = request.form.get('url')
    use_tide.start(url)
    web = WebFinger(url.replace('https://', '').replace('http://', ''), 0)
    web.run()
    """
    with open('finger.txt', 'r') as f:
        finger = f.read()
    """
    return render_template('index.html')

@app.route('/input5',methods = ['POST'])
def input5():
    global name
    http = request.form.get('list')
    ip = request.form.get('ip')
    if(http == '1'):
        db_conn = pymysql.connect(host="localhost", user="root", password="", db="vul", charset="utf8")
        cur = db_conn.cursor()
        # 执行sql语句
        try:
            # 执行sql语句
            sql = "insert into vul values('%s','%s','xray','%s','expired' )" % (
                str(time.time()),str(time.asctime(time.localtime(time.time()))), ip)
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
        xray(ip)
        return render_template('alert-2.html', data=datalist)
        result=''
    if(http == 'a'):
        #os.system能查看结果
        result = os.popen('python ./pocsuite3-master/pocsuite3/cli.py -r ./pocsuite3-master/pocsuite3/pocs/telnet_burst.py -u '+ip)
    if (http == 'b'):
        result = os.popen(
            'python ./pocsuite3-master/pocsuite3/cli.py -r ./pocsuite3-master/pocsuite3/pocs/thinkphp_rce2.py -u ' + ip)
    if (http == 'c'):
        result = os.popen(
            'python ./pocsuite3-master/pocsuite3/cli.py -r ./pocsuite3-master/pocsuite3/pocs/redis_unauthorized_access.py -u ' + ip)
    if (http == 'd'):
        result = os.popen(
            'python ./pocsuite3-master/pocsuite3/cli.py -r ./pocsuite3-master/pocsuite3/pocs/node_red_unauthorized_rce.py -u ' + ip)
    if (http == 'e'):
        result = os.popen(
            'python ./pocsuite3-master/pocsuite3/cli.py -r ./pocsuite3-master/pocsuite3/pocs/weblogic_cve_2017_10271_unserialization.py -u ' + ip)
    #print(http)
    #print(ip)
    if result == '':
        context = ''
    else:
        context = result.read()
    if('failed' in context):
        db_conn = pymysql.connect(host="localhost", user="root", password="", db="vul", charset="utf8")
        if(http == 'a'):
            name='Telnet 弱口令'
        if (http == 'b'):
            name='Thinkphp 5.0.x 远程代码执行漏洞'
        if (http == 'c'):
            name='Redis未授权访问'
        if (http == 'd'):
            name='Node-RED 未授权远程命令执行'
        if (http == 'e'):
            name='Weblogic 10.3.6 wls-wsat XMLDecoder 反序列化漏洞'
        # 创建游标对象
        cur = db_conn.cursor()
        # 执行sql语句
        try:
            # 执行sql语句
            sql = "insert into vul values('%s','%s','%s','%s','%s')" % (str(time.time()),str(time.asctime( time.localtime(time.time()))), name, ip, 'not vul')
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
        print('不存在漏洞')
    if ('incorrect' in context):
        db_conn = pymysql.connect(host="localhost", user="root", password="", db="vul", charset="utf8")
        if (http == 'a'):
            name = 'Telnet 弱口令'
        if (http == 'b'):
            name = 'Thinkphp 5.0.x 远程代码执行漏洞'
        if (http == 'c'):
            name = 'Redis未授权访问'
        if (http == 'd'):
            name = 'Node-RED 未授权远程命令执行'
        if (http == 'e'):
            name = 'Weblogic 10.3.6 wls-wsat XMLDecoder 反序列化漏洞'
        # 创建游标对象
        cur = db_conn.cursor()
        # 执行sql语句
        try:
            # 执行sql语句
            sql = "insert into vul values('%s','%s','%s','%s','%s')" % (
            str(time.time()),str(time.asctime(time.localtime(time.time()))), name, ip, 'IP或URL输入错误')
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
        print('参数输入错误')

    if(('failed' not in context) and ('incorrect' not in context)):
        db_conn = pymysql.connect(host="localhost", user="root", password="", db="vul", charset="utf8")
        if (http == 'a'):
            name = 'Telnet 弱口令'
        if (http == 'b'):
            name = 'Thinkphp 5.0.x 远程代码执行漏洞'
        if (http == 'c'):
            name = 'Redis未授权访问'
        if (http == 'd'):
            name = 'Node-RED 未授权远程命令执行'
        if (http == 'e'):
            name = 'Weblogic 10.3.6 wls-wsat XMLDecoder 反序列化漏洞'
        # 创建游标对象
        cur = db_conn.cursor()
        # 执行sql语句
        try:
            # 执行sql语句
            sql = "insert into vul values('%s','%s','%s','%s','%s')" % (
                str(time.time()),str(time.asctime(time.localtime(time.time()))), name, ip, 'vul')
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
        print('成功')

        #发送邮箱
        msg_from = 'ft1374076342@163.com'  # 发送方邮箱
        passwd = 'BJJFXRHJMCGYNJJU'  # 填入发送方邮箱的授权码
        with open('setting.txt','r') as f:
            if(f is not None):
                """
                str_content = f.read()
                s1 = re.finditer(r".*?;", str_content)
                for match in s1:
                    ret1 = match.group()
                    print(ret1.replace(';', ''))

                s2 = re.finditer(r";.*?", str_content)
                for match in s2:
                    ret2 = match.group()
                    print(ret2.replace(';', ''))
                """
                msg_to = f.read()
                print(msg_to)
        #msg_to = "ft1374076342@163.com"  # 收件人邮箱
        subject = "发现漏洞: "+name  # 主题
        content = "来自Matoi交互扫描器的提示：\n" \
                  "\n"+ip+" 存在"+name+""\
                  "请及时查看并修复漏洞！"  # 正文
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to
        try:
            s = smtplib.SMTP_SSL("smtp.163.com", 465)  # 邮件服务器及端口号
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print('发送成功')
        except:
            print('发送失败')
            s.quit()
    return render_template('index.html')

@app.route('/list_attack')
def list_attack():
    datalist = []
    # 建立数据库连接
    db_conn = pymysql.connect(host="localhost", user="root", password="", db="vul", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "select * from vul where id in (select max(id) from vul group by time) order by name desc,id desc;"
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
    return render_template('attack_result.html', data=datalist)

@app.route('/download')
def download():
    # 建立数据库连接
    db_conn = pymysql.connect(host="localhost", user="root", password="", db="xray", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "SELECT distinct id,ip FROM name order by id desc"
        # sql = "SELECT * FROM result where id = 1"
        print(sql)
        # 执行SQL语句
        db_conn.ping(reconnect=True)
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        name = str(results[0][0])+'.html'
        print('name: '+name)
        # 事物提交
        db_conn.commit()

    except Exception as err:
        print("sql语句执行错误", err)
        db_conn.rollback()
    db_conn.close()
    try:
        response = make_response(send_file(name))
        response.headers["Content-Disposition"] = "p_w_upload; filename="+name+';'
        return response
    except Exception as err:
        return render_template('alert.html')

@app.route('/finger_result')
def finger_result():
    # 建立数据库连接
    datalist=[]
    db_conn = pymysql.connect(host="localhost", user="root", password="", db="finger", charset="utf8")

    # 创建游标对象
    cur = db_conn.cursor()
    # 执行sql语句
    try:
        # 执行sql语句
        sql = "SELECT distinct id,url,result1,result2 FROM finger order by id desc"
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
    return render_template('finger_result.html', data=datalist)

@app.route('/input6',methods = ['POST'])
def set():
    email = request.form.get('email')
    print(email)
    with open('setting.txt','w') as f:
        if(email == None):
            return render_template('alert-3.html')
        else:
            f.write(email)
            return render_template('index.html')
"""
    if(email == ''):
    if(url == ''):

@app.route('/input7',methods = ['POST'])
def xray_push():
    os.popen('python xray_push.py')
    return render_template('index.html')
"""

if __name__ == '__main__':
    app.run(threaded=True,port=8000)