#coding=utf-8

from ENV.MsSql import ODBC_MS
from SettingDataBase import SqlServerSetting
from SettingSQL import SqlFiles, NewGameRoomSql
from SettingRooms import room_list
from ENV import CreateGameStoreInfo
import sys

# -------------------------------------------------------------------------------
# Purpose: Ms sql server exec sql file
# Tips: 要在Setting里面设置好数据库配置
# Author: Zhushw
# -------------------------------------------------------------------------------
from UI.SaveToSettingFile_Python2 import zsw_python2_3_unicode_str
# from UI.SaveToSettingFile_Python3 import zsw_python2_3_unicode_str
# gServerId = ""

def main(argv):
    # --------------------连接数据库----------------------
    ms = ODBC_MS('{SQL SERVER}', SqlServerSetting.SERVER_ADRESS, SqlServerSetting.DATABASE, SqlServerSetting.UID,SqlServerSetting.PWD)
    # print (argv)

    # # --------------开服 Game Room Info Sql------------------------
    if '-m' in argv:
    # if True:
        for i in room_list:
            # print i.ServerID
            CreateRoomInfoF(ms, i.GameRoomListIndex, i.ServerID, i.ServerName, i.ServerPort, i.ServerMachine)

    # --------------开服 game store info sql------------------------
    if '-s' in argv:
    # if True:
        for i in room_list:
            CreateGameStoreF(ms, i.ServerID, i.AndroidCount)


    # --------------读取添加机器人sql文件------------------------
    if '-r' in argv:
    # if True:
        for i in room_list:
            CreateSqlRobotF(ms, i.SqlFileRobotListIndex, i.ServerID, i.AndroidCount)




def CreateRoomInfoF(ms, GameRoomListIndex, ServerID, ServerName, ServerPort, ServerMachine):
    # --------------开服 Game Room Info Sql------------------------
    print(u"---------------Game Room Info 开始处理!!!------------------")
    with open('create_room/' + NewGameRoomSql[GameRoomListIndex], 'r') as f:
        sql_f = f.read()

    # print(sql_f)
    sql_f = sql_f % (ServerID, ServerName, str(int(ServerID)+10000), ServerMachine)     # 把端口号设置成10000+ServerID

    sql_f = zsw_python2_3_unicode_str(sql_f)
    print(sql_f)

    re = ms.ExecQueryExp(sql_f)
    print(re[0][0])

    print(u'---------Game Room 表插入完毕 ---------')


def CreateGameStoreF(ms, ServerID, AndroidCount):
    # --------------开服 game store info sql------------------------
    print(u"--------------------------game store info 开始处理!!!------------------")
    print(u"房间ID：%s"% ServerID)
    gameStoreSql = CreateGameStoreInfo.makeGameStoreInfoSql(ServerID, AndroidCount)

    gameStoreSql = zsw_python2_3_unicode_str(gameStoreSql)
    # print(gameStoreSql)
    re = ms.ExecQueryExp(gameStoreSql)
    print(u"房间StoreInfo："+ str(re[0][0]) + u"已经成功插入！")
    print(u'---------Game Store 表插入完毕 ---------')


def CreateSqlRobotF(ms, SqlFileRobotListIndex, ServerID, AndroidCount):
    # --------------读取添加机器人sql文件------------------------
    print(u"------------------------------开始添加机器人!!!---------------------------------")

    # 循环遍历加入机器人，因为之前sql内循环时间太久，pyodbc执行不完就断了，所以改为外部实现循环
    for i in range(0, AndroidCount):

        with open('sql_files/' + SqlFiles[SqlFileRobotListIndex], 'r') as f:
            sql_f = f.read()

        sql_f = sql_f.format(serverID=ServerID, num=i)
        sql_f = zsw_python2_3_unicode_str(sql_f)
        print(i)
        # 执行sql文件
        ms.ExecNoQuery(sql_f)

    # --------------end-----------------------
    print(u'---------添加机器人执行完毕 ---------')





if __name__ == '__main__':
    main(sys.argv[1:])

