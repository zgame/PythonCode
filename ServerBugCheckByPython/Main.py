# -*- coding: UTF-8 -*-

import threading
import time
import Receive
import Send

from unit.CaseHall import *
from unit.CaseFishPond import *
from unit.CaseMiniGame import *
from unit.MainBY_210 import *

import Setting

def recv_loop(s):
    while True:
        # print("receive")
        msg = s.recv(1024 * 80)  # 接收字节的数据
        # print("msg", msg)
        buf_len = len(msg)
        buf_head = 0
        while buf_head < buf_len:
            deal_buffer = msg[buf_head:buf_len]
            main_cmd, sub_cmd, buffer_size, ver = Receive.deal_recv_tcp_deader_data(deal_buffer)
            buf_head = buf_head + buffer_size + 10
            Receive.deal_recv_protocol_data(main_cmd, sub_cmd, deal_buffer[10:10+buffer_size], buffer_size)
        # time.sleep(0.2)


def send_loop(s):
    count=0
    while True:
         if Receive.SendStart or Setting.ChoiceServer=="游戏服":
            send_msg_loop_start()
            time.sleep(0.2)  # 每隔0.3秒
            ##下面注释代码为服务器过滤
            # count=count+1
            # print("count:",count)
            # if count==50:
            #     time.sleep(5)
            #     count=0

# pass


# ----------------------------------------------发送列表-------------------------------------------------
# 这里是发送消息的列表
def send_msg_loop_start():
    if Setting.ChoiceServer=="登录服":
        send_ls()
    elif Setting.ChoiceServer=="游戏服":
        send_gs()
    #把要测试的协议函数写到这里， 会循环的发送


#协议集合
def send_ls(): #大厅协议集合
    MainBY210.send_msg_cannon_equip()
    MainBY210.send_msg_connon_compound()
    MainBY210.send_msg_cannon_renew()
    MainBY210.send_msg_cannon_buy()
    MainBY210.send_msg_GetRechargeRebate()
    MainBY210.send_msg_usre_info_ls()
    pass

def send_gs():#游戏服协议集合
    MainBY210.send_msg_cannon_equip()
    MainBY210.send_msg_connon_compound()
    MainBY210.send_msg_cannon_renew()
    MainBY210.send_msg_cannon_buy()
    MainBY210.send_msg_GetRechargeRebate()
    MainBY210.send_msg_usre_info_gs()
    pass


def main():
    print("---------start!---------")
    global GlobalSocket


    if Setting.ChoiceServer=="登录服":
        GlobalSocket = Send.get_socket_login_server()
        Send.send_msg_login()         # 申请登录服务器

    elif Setting.ChoiceServer=="游戏服":
        print("登录游戏服")
        GlobalSocket = Send.get_socket_game_server()
        Send.send_msg_game_login()



    thread1 = threading.Thread(target=recv_loop, args=(GlobalSocket,))
    thread1.start()

    thread2 = threading.Thread(target=send_loop, args=(GlobalSocket,))
    thread2.start()

    # s.close()
    # print("---------end!---------")

if __name__ == "__main__":
    main()


