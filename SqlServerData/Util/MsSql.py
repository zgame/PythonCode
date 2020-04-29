#coding=utf-8
# SQL SERVER
# !/usr/bin/python

# -------------------------------------------------------------------------------
# Purpose: Ms sql server op
# Tips: python 3.6
#       pip install pyodbc
#       数据库需要在Sql Server Configuration Manager里面将TCP/IP协议开启
# Author: Zhushw
# -------------------------------------------------------------------------------
import pyodbc



class ODBC_MS:
    ''' 对pyodbc库的操作进行简单封装
    pyodbc库的下载地址:http://code.google.com/p/pyodbc/downloads/list
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启
    此类完成对数据库DB的连接/查询/执行操作
    正确的连接方式如下:
    cnxn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=ZHANGHUAMIN\MSSQLSERVER_ZHM;DATABASE=AdventureWorks2008;UID=sa;PWD=wa1234')
    cnxn = pyodbc.connect(DRIVER='{SQL SERVER}',SERVER=r'ZHANGHUAMIN\MSSQLSERVER_ZHM',DATABASE='AdventureWorks2008',UID='sa',PWD='wa1234',charset="utf-8")
    '''

    def __init__(self, DRIVER, SERVER, DATABASE, UID, PWD):
        ''' initialization '''

        self.DRIVER = DRIVER
        self.SERVER = SERVER
        self.DATABASE = DATABASE
        self.UID = UID
        self.PWD = PWD

    def __GetConnect(self):
        ''' Connect to the DB '''

        if not self.DATABASE:
            raise (NameError, "no setting db info")

        self.conn = pyodbc.connect(DRIVER=self.DRIVER, SERVER=self.SERVER, DATABASE=self.DATABASE, UID=self.UID,
                                   PWD=self.PWD, charset="UTF-8")
        # self.conn = pyodbc.connect(DRIVER=self.DRIVER, SERVER=self.SERVER, DATABASE=self.DATABASE, UID=self.UID, PWD=self.PWD)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "connected failed!")
        else:
            return cur

    def ExecQuery(self, sql):
        ''' select 返回值 ，只用来查询， 并不修改数据库'''

        cur = self.__GetConnect()  # 建立链接并创建数据库操作指针
        cur.execute(sql)  # 通过指针来执行sql指令
        ret = cur.fetchall()  # 通过指针来获取sql指令响应数据
        cur.close()  # 游标指标关闭
        self.conn.close()  # 关闭数据库连接

        return ret

    def ExecQueryExp(self, sql):
        ''' insert带返回值，需要sql增加 set nccount on去掉影响行数的返回
              后面加上select @@identity              '''

        cur = self.__GetConnect()  # 建立链接并创建数据库操作指针
        cur.execute(sql)  # 通过指针来执行sql指令
        ret = cur.fetchall()  # 通过指针来获取sql指令响应数据
        self.conn.commit()
        cur.close()  # 游标指标关闭
        self.conn.close()  # 关闭数据库连接

        return ret


    def ExecNoQuery(self, sql):
        '''  insert等修改数据库的操作，不带返回值 '''

        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()  # 连接句柄来提交
        cur.close()
        self.conn.close()
