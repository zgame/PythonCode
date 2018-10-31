# -*- coding: UTF-8 -*-


import struct

import Send
from const.protocol_ls import *
from const.protocol_cs import *
from const.protocol_gs import *
from proto.CMD_LoginServer_pb2 import *
from proto.CMD_Game_pb2 import *
from proto.CMD_GameServer_pb2 import *


SendStart = False



# TCPHead定义
cbDataKind = 0  # //数据类型
cbCheckCode = 1  # //效验字段
wPacketSize = 2  # //数据大小
wMainCmdID = 3  # // 主命令码
wSubCmdID = 4  # 子命令码
wPacketVer = 5  # // 封包版本号


# 获取TCPHead头部信息
def deal_recv_tcp_deader_data(msg):
    s1 = struct.unpack("BBhhhh", msg[:10])
    # print(s1)
    buffer_size = s1[wPacketSize]
    sub_cmd = s1[wSubCmdID]
    main_cmd = s1[wMainCmdID]
    ver = s1[wPacketVer]

    return main_cmd, sub_cmd, buffer_size,ver

# 按照子命令分类，处理protocol数据包
def deal_recv_protocol_data(main_cmd, sub_cmd, buffer, buffer_size):
    # print("getMsg")
    if main_cmd == MDM_MB_LOGON:
        if sub_cmd == SUB_MB_LOGON_SUCCESS:
            print("登录成功")
            # 处理登录成功
            msg = CMD_MB_LogonSuccess()
            msg.ParseFromString(buffer)
            print "---------------玩家的ID：",msg.user_id
            print "-----------玩家的金币为：",msg.user_score
            print "-----------玩家的钻石为：",msg.user_diamond
            print "-----------玩家的鱼劵为：",msg.user_lottery
            print "-----------玩家的等级为：",msg.level
            print "--------玩家的VIP等级为：",msg.vip_lev

            global SendStart
            SendStart = True

        elif sub_cmd == SUB_MB_LOGON_FAILURE:
            print("登录失败")
        elif sub_cmd == SUB_MB_LOGON_FINISH:
            # print("登录完成_receive")
            pass


    elif main_cmd == MDM_MB_GIFT_PACK:
        if sub_cmd == SUB_MB_L2C_GIFT_PRODUCT_INFO:
            print("礼包")
    elif main_cmd == MDM_MB_ACTIVITY:
        if sub_cmd == SUB_MB_S2C_ACTIVITY:
            print("活动")
        elif sub_cmd == SUB_MB_S2C_ACTIVITY_CELL_INFO_LIST:
            print("活动")
    elif main_cmd == MAIN_CHAT_CMD:
        if sub_cmd == SUB_S_LOGIN:
            print("聊天")
    elif main_cmd == MDM_MB_VIP:
        if sub_cmd == SUB_MB_S_VIP_INFO:
            print("vip ------")

    elif main_cmd == MDM_MB_SERVER_LIST:
        if sub_cmd == SUB_MB_LIST_SERVER:
            print("服务器列表")
        elif sub_cmd == SUB_MB_LIST_FINISH:
            print("房间信息完成 ------")
    elif main_cmd == MDM_MB_USER_INFO:
        if sub_cmd == SUB_MB_S_GET_CHAT_SERVER_INFO:
            print("聊天")
        elif sub_cmd == SUB_MB_S_USER_MATERIAL_OBJECT:
            print("玩家信息完成 ------")
        elif sub_cmd == SUB_MB_S_REQUEST_ARENA:
            print("竞技场数据 ------")
    elif main_cmd == MDM_GR_LOGON:
        # SendStart = True
        if sub_cmd == SUB_GR_LOGON_FAILURE:
            print("登录失败")
            msg = CMD_GR_LogonFailure()
            print ("error_code",msg.error_code)
            print ("error_code",msg.describe)
        elif sub_cmd == SUB_GR_LOGON_SUCCESS:
            print("game登录成功 ------")
            # Send.enterScene()  # 进入场景开始
        elif sub_cmd == SUB_GR_LOGON_FINISH:
            print("game登录完成 ------")
            Send.enterScene()   # 进入场景开始

    elif main_cmd == MDM_GF_GAME:
       # print("getMsg  MDM_GF_GAME-------",sub_cmd)
        if sub_cmd == SUB_S_GET_ALMS:
            msg = CMD_S_GET_ALMS()

            print("获取救济金----------------------")
            print(msg.get_result)
            print(msg.get_score)
            print(msg.wait_time)
        # elif sub_cmd == SUB_GR_LOGON_FINISH:
        #     print("game登录完成 ------")

    return buffer_size+10


