import urllib
import pymysql

def main():
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
    return zip(datalist,datalist2)
    # 获得了整个网页的内容也就是源代码
    #print(str(contents))