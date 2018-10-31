# -*- coding: UTF-8 -*-

from proto.CMD_LoginServer_pb2 import *
from const.protocol_ls import *
import Setting

from Send import SendFunc

class PlayActionMiniGame(object):
    def __init__(self):
        self.userid= Setting.UserID

#下载小游戏获得金币
    def send_msg_download_mini_game(self):
        cmd=CMD_C_download_mini_game()
        cmd.GameID=1 #枚举 对应游戏ID
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_DOWNLOAD_GAME,s)
        print("下载小游戏获得金币")




CaseMiniGame=PlayActionMiniGame()