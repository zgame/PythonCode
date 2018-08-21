# coding=utf-8

# -------------------------------------------------------------------------------
# 配置数据
# Author: Zhushw

# 运行环境需求:
# python 2.7 + pyodbc
# 安装pyodbc : pip install pyodbc
# 数据库需要在Sql Server Configuration Manager里面将TCP/IP协议开启
# -------------------------------------------------------------------------------

class SqlServerSetting:
    # 数据库的IP地址
    SERVER_ADRESS = r'9999999'
    # 数据库名字
    DATABASE = 'DataBaseBY'
    # 登录名
    UID = 'sa'
    # 登录密码
    PWD = '999999999Aa123456'

