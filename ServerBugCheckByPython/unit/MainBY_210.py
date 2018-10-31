# -*- coding: UTF-8 -*-
import random
from proto.CMD_Common_pb2 import *
from proto.CMD_GlobalServer_pb2 import *
import Setting
from Send import SendFunc


class PlayActionMainBY_210(object):
    def __init__(self):
        self.userid=Setting.UserID
        print(self.userid)
#----------------------炮台道具协议 Start

    #玩家请求装备炮台
    def send_msg_cannon_equip(self):
        cmd=CMD_C_Cannon_Equip()
        testNumList = [3101,3102,3103,3104,3105]
        cmd.cannon_id= testNumList[random.randint(0,len(testNumList)-1)] #要装备的炮台id
        cmd.cannon_num= testNumList[random.randint(0,len(testNumList)-1)]#炮管数量
        cmd.cannon_mulriple= testNumList[random.randint(0,len(testNumList)-1)]#炮倍
        s = cmd.SerializeToString()
        SendFunc(98,2,s)
        print("玩家请求装备炮台")

    #玩家请求合成炮台
    def send_msg_connon_compound(self):
        cmd=CMD_C_Cannon_Compound()
        cmd.cannon_id=3101 #炮台的模板id
        cmd.valid_id=2 #时间id
        s = cmd.SerializeToString()
        SendFunc(98,4,s)
        print("玩家请求合成炮台")

    #玩家请求炮台续期
    def send_msg_cannon_renew(self):
        cmd=CMD_C_Cannon_Renew()
        cmd.cannon_id=3105 #炮台物品id
        cmd.valid_id=6 #有效期表的id，用来表示续哪个期限，花多少钱
        s = cmd.SerializeToString()
        SendFunc(98,6,s)
        print("玩家请求炮台续期")

    #玩家请求购买炮台
    def send_msg_cannon_buy(self):
        cmd=CMD_C_Cannon_Buy()
        cmd.cannon_id=3103 #炮台物品id
        cmd.valid_id=4 #有效期表的id，用来表示续哪个期限，花多少钱
        s = cmd.SerializeToString()
        SendFunc(98,8,s)
        print("玩家请求购买炮台")
#----------------------炮台道具协议 End
#---
#-----------------礼包和返利协议 Start
    #领取充值返利礼包
    def send_msg_GetRechargeRebate(self):
        cmd=CMD_C_GetRechargeRebate()
        testNumList = [1, 2, 4, 8, 16,32,64,128]
        cmd.ID=testNumList[random.randint(0,len(testNumList)-1)] #礼包ID
        s = cmd.SerializeToString()
        SendFunc(102,326,s)
        print("领取充值返利礼包")

    #发送点击礼包次数(游戏服)
    def send_msg_usre_info_gs(self):
        cmd=CMD_C_RecordOpenGiftCount()
        testNumList = [1, 101, 801, 1001, 3001, 3101, 3102]
        testNumList1 = [1, 2, 3, 4, 5, 6, 7]
        cmd.count=testNumList[random.randint(0,len(testNumList)-1)] #点击次数
        cmd.id=testNumList1[random.randint(0,len(testNumList)-1)] #礼包ID
        s = cmd.SerializeToString()
        SendFunc(3,111,s)
        print("发送点击礼包次数(游戏服)")

    #发送点击礼包次数(登录服)
    def send_msg_usre_info_ls(self):
        cmd=CMD_C_RecordOpenGiftCount()
        testNumList = [1, 101, 801, 1001, 3001, 3101, 3102]
        testNumList1 = [1, 2, 3, 4, 5, 6, 7]
        cmd.count=testNumList[random.randint(0,len(testNumList)-1)] #点击次数
        cmd.id=testNumList1[random.randint(0,len(testNumList)-1)] #礼包ID
        s = cmd.SerializeToString()
        SendFunc(102,328,s)
        print("发送点击礼包次数(登录服)")
#--------------------礼包和返利协议 End

MainBY210=PlayActionMainBY_210()