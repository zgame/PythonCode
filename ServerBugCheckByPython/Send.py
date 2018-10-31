# -*- coding: UTF-8 -*-
import struct
import hashlib
# import Receive
import Setting
import socket
from const.protocol_gs import *
from const.protocol_ls import *
from proto.CMD_Common_pb2 import *
from proto.CMD_GameServer_pb2 import *
from proto.CMD_LoginServer_pb2 import *

# def send_gm_cmd(server_id, cmd):
#     send_cmd = MonitorCMD.CMD_MONITOR_CMD()
#     send_cmd.server_id = int(server_id)
#     send_cmd.cmd = cmd.encode(encoding="gb2312")
#     # print(send_cmd)
#     buffer_cmd = send_cmd.SerializeToString()
#     # print(buffer_cmd)
#     SendFunc(MAIN_CMD_ID, SUB_C_MONITOR_CMD, send_cmd)


GlobalSocket = None

# 登录服务器socket
def get_socket_login_server():
    global GlobalSocket
    GlobalSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = socket.gethostname()
    from Setting import LoginServer, LoginServerPort
    # host = "192.168.0.218"
    # port = 8330
    GlobalSocket.connect((LoginServer, LoginServerPort))
    return GlobalSocket

# 游戏服务器socket
def get_socket_game_server():
    global GlobalSocket
    GlobalSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = socket.gethostname()
    from Setting import GameServer, GameServerPort
    # host = "192.168.0.218"
    # port = 8330
    GlobalSocket.connect((GameServer, GameServerPort))
    return GlobalSocket



# ------------------------------------------------基础函数-----------------------------------------------
TokenNum = 0
# 发送数据包
def SendFunc(main, sub, buffer_cmd):
    global TokenNum
    buffer_token = struct.pack("H", TokenNum)
    TokenNum = TokenNum + 1

    size = len(buffer_cmd)
    buffer_Head = get_send_tcp_header_data(main, sub, size)
    # print(buffer_Head)

    # print(buffer_Head + buffer_cmd)
    # s = Receive.GlobalSocket

    buffer = buffer_Head + encrypt(buffer_token + buffer_cmd)
    GlobalSocket.send(buffer)  # 发送 头部数据 + 加密之后的（token + msg）
    # print('send gm cmd')


def encrypt(s):
    # return s
    lst = []
    length = len(s)
    for i in range(length):
        tmp = length - i
        c = ord(s[i])
        c ^= 0xE9 * tmp + tmp % 14
        lst.append(chr(c % 256))
    return ''.join(lst)




# 组合成数据包头部
def get_send_tcp_header_data(maincmd, childcmd, size):
    buffer_t = struct.pack("BBhhhh", 0, 1, size + 2, maincmd, childcmd, 1)  # size+2 是因为有token， 最后一位是1，表示有token
    return buffer_t





# ------------------------------------------------单独的每个协议-----------------------------------------------
# 发送登录请求(登录服)
def send_msg_login():
    cmd = CMD_MB_GuestLogin()
    cmd.machine_id = Setting.MacAddress
    cmd.ditch_number = 9
    cmd.client_kind = 3
    cmd.game_kind_id = 8
    cmd.plaza_version = 0
    cmd.ip_addr = "127.0.0.1"
    cmd.device_type = "virtual"
    s = cmd.SerializeToString()
    SendFunc(MDM_MB_LOGON, SUB_MB_GUESTLOGIN, s)

# 发送请求例子， 新的协议和参数写的例子， 写好之后，添加到上面去做循环发送



############################
#大厅相关协议 CaseHall.py
#鱼池相关协议 CaseFishPond.py
#小游戏相关协议 CaseMiniGame.py
#GameScoreChangeRecord 金币、钻石、道具流水表
#GameDiamodChangeRecord
#GameItemChangeRecord
###########################


# 登录游戏服务器（游戏服）
def send_msg_game_login():
    cmd = CMD_GR_LogonUserID()

    cmd.plaza_version = 0
    cmd.frame_version = 101056515
    cmd.process_version = 101056515
    cmd.client_type = 3
    cmd.user_id = Setting.UserID
    cmd.password = get_pwd(Setting.MacAddress, Setting.UserID)
    cmd.machine_id = Setting.MacAddress
    cmd.kind_id = 3
    cmd.ip_addr = "127.0.0.1"
    cmd.ditch_number = 9
    cmd.device_type = "virtual"
    cmd.packet_index = 1
    cmd.is_android = 0
    cmd.cannon_mulriple = 0



    s = cmd.SerializeToString()
    # SendFunc(MDM_MB_LOGON, SUB_MB_GUESTLOGIN, s)
    SendFunc(MDM_GR_LOGON, SUB_GR_LOGON_USERID, s)
    #print "9999"


# 生成游客登录密码(gs)
def get_pwd(machine_id, user_id):
    blanks = []
    cnt = 32 - len(machine_id)
    if cnt > 0:
        for i in range(cnt):
            blanks.append(' ')
    temp = machine_id + ''.join(blanks) + str(user_id)
    uni_str = temp.decode('utf-8')
    buf = ''
    for e in uni_str:
        buf += struct.pack('H', ord(e))
    md = hashlib.md5()
    md.update(buf)
    return str(md.hexdigest()).upper()

# 进入场景
def enterScene():
    print("send enterScene")
    cmd = CMD_GF_GameOption()
    cmd.allow_lookon = 0
    cmd.frame_version = 0
    cmd.client_version = 101056515

    s = cmd.SerializeToString()
    SendFunc(MDM_GF_FRAME, SUB_GF_GAME_OPTION, s)

