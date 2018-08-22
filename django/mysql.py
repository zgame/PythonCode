import pymysql

def get_sql_data(sql):
    # 打开数据库连接
    # db = pymysql.connect("55a0ed1bee1a4.sh.cdb.myqcloud.com:6370", "root", "***", "test")
    db = pymysql.connect("127.0.0.1", "zsw1", "zsw123", "by_statis_db")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    # print("Database version : %s " % data)
    db.close()

    return data
