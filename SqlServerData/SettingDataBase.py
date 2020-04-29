# coding=utf-8

# -------------------------------------------------------------------------------
# 配置数据
# Author: Zhushw

# 运行环境需求:
# python 3.7 + pyodbc
# 安装pyodbc : pip install pyodbc
# 数据库需要在Sql Server Configuration Manager里面将TCP/IP协议开启
# -------------------------------------------------------------------------------

class SqlServerSetting:
    # 数据库的IP地址
    SERVER_ADRESS = r'17299.1699.14099.15399'
    # 登录名
    UID = 'dbuser_ro'
    # 登录密码
    PWD = '35A20E7966ECDC93'

    # 平台数据库名字
    DATABASE_Platform = 'PlatformDB_201912'
    # 日志数据库名字
    DATABASE_Log = 'BY_LOG_201912'