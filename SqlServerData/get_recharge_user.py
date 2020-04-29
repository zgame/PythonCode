from Util.MsSql import ODBC_MS
from SettingDataBase import SqlServerSetting


# --------------------连接平台数据库， 获取充值记录----------------------
database_platform = ODBC_MS('{SQL SERVER}', SqlServerSetting.SERVER_ADRESS, SqlServerSetting.DATABASE_Platform, SqlServerSetting.UID,
                            SqlServerSetting.PWD)


# 查询一段时间之内的充值情况   2020年1月9日全天的充值记录
sql_fp = "SELECT * FROM PPayCoinOrder_All WHERE SuccessTime >= '1578499200' and SuccessTime <= '1578585600'"

rep = database_platform.ExecQueryExp(sql_fp)
print("------------------------获取充值记录-------------------------------")
print(rep[0])


# --------------------连接日志数据库， 查询日志记录----------------------
database_log = ODBC_MS('{SQL SERVER}', SqlServerSetting.SERVER_ADRESS, SqlServerSetting.DATABASE_Log, SqlServerSetting.UID,
                            SqlServerSetting.PWD)

# 用户id  22890040 的金币流水
sql_f = "SELECT * FROM GameScoreChangeRecord_20200109 WHERE UserID = '22890040'"


# 用户id  22890040 的混合流水
sql_f = "SELECT * FROM HunGameChipRecord_20200109 WHERE UserID = '22890040'"


re = database_log.ExecQueryExp(sql_f)
print("------------------------金币流水-------------------------------")
print(re[0])
print(re[0][0])
