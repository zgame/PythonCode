#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("55a0ed1bee1a4.sh.cdb.myqcloud.com:6370", "root", "***", "test")
# db = pymysql.connect("127.0.0.1", "zsw1", "zsw123", "zsw_new_schema")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

try:
    # 执行SQL语句
    cursor.execute("select * FROM test_ip ")
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        ip = row[0]
        # 打印结果
        print("ip=%s" % (ip))

    # 执行sql语句
    cursor.execute("INSERT INTO test_ip(ip)VALUES ('222233222')")
    # 提交到数据库执行
    db.commit()

except:
    print("Error: unable to fecth data")

# 关闭数据库连接
db.close()
