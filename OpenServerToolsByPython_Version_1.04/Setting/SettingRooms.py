# coding=utf-8

# -------------------------------------------------------------------------------
# 配置开房间的数据
# Author: Zhushw

# 运行环境需求:
# python 2.7 + pyodbc
# 安装pyodbc : pip install pyodbc
# 数据库需要在Sql Server Configuration Manager里面将TCP/IP协议开启
# -------------------------------------------------------------------------------


# 要建立的房间的配置信息
# ServerID = "2058"  # 房间的ID , 这个正常不用管， 如果单独添加GameStoreInfo就需要
# ServerName = "测试测试用例"  # 房间名字
# ServerPort = "100099999"  # 房间端口号
# ServerMachine = "****************"  # 机器码
# AndroidCount = 40  # 添加机器人的数量
# GameRoomListIndex = 0  # 要创建房间类型的编号， 上面的对应编号
# SqlFileRobotListIndex = 0  # 要加入机器人的sql编号，上面的对应编号


class RoomSetting:
    def __init__(self, ServerID, ServerName, ServerPort, ServerMachine, AndroidCount, GameRoomListIndex, SqlFileRobotListIndex):
        self.ServerID = ServerID
        self.ServerName = ServerName
        self.ServerPort = ServerPort
        self.ServerMachine = ServerMachine
        self.AndroidCount = AndroidCount
        self.GameRoomListIndex = GameRoomListIndex
        self.SqlFileRobotListIndex = SqlFileRobotListIndex




room_list = [
    # 要配置的房间的信息， 可以一次性配置N多房间， 在列表后面增加即可
    #          房间的ID    房间名字        端口号        机器码      机器人的数量  要创建房间类型的编号   要加入机器人的sql编号
    RoomSetting("101", "满贯捕鱼百人牛牛[101]_1.12", "作废了", "95200C61D8ECAA14E38836C6526BDBF0",    20,             10,                  5),

]
