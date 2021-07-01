import time

# 建立数据库连接
import pymysql

db_conn = pymysql.connect(host="localhost", user="root", password="", db="port_scan", charset="utf8")

# 创建游标对象
cur = db_conn.cursor();

# 执行sql语句
try:
    # 执行sql语句
    sql = "insert into result values('%s','%s',%d)" % (time.time(),'192.168.1.0',6379)
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