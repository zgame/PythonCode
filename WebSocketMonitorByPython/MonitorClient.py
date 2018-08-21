import socket
import struct
import threading
import time
import iniparser

import BY_proto.CMD_Monitor_pb2 as MonitorCMD
from MonitorUI import open_ui, refresh_server_list_info, add_server_list, del_server_list

# TCPHead定义
cbDataKind = 0  # //数据类型
cbCheckCode = 1  # //效验字段
wPacketSize = 2  # //数据大小
wMainCmdID = 3  # // 主命令码
wSubCmdID = 4  # 子命令码
wPacketVer = 5  # // 封包版本号

# 主命令定义
MAIN_CMD_ID = 1100

# 子命令定义
SUB_C_MONITOR_REG = 10  # // 注册为客户端
SUB_S_MONITOR_ITEMS = 100  # // 下发服务器列表
SUB_S_MONITOR_STATE = 101  # // 更新状态
SUB_S_MONITOR_LOG = 103  # // 添加日志
SUB_S_NEW_MONITOR_ITEM = 104  # // 新增服务器
SUB_S_DEL_MONITOR_ITEM = 105  # // 删除服务器
SUB_C_MONITOR_KEEPLIVE = 200  # // 心跳包
SUB_S_MONITOR_KEEPLIVE = 201  # // 心跳包
SUB_C_MONITOR_CMD = 2050  # // 执行命令
SUB_S_MONITOR_CMD = 2051  # // 执行命令结果




# 获取TCPHead头部信息
def deal_recv_tcp_deader_data(msg):
    s1 = struct.unpack("BBHHHH", msg[:10])
    print(s1)
    buffer_size = s1[wPacketSize]
    sub_cmd = s1[wSubCmdID]

    return sub_cmd, buffer_size


# 按照子命令分类，处理protocol数据包
def deal_recv_protocol_data(sub_cmd, msg, buffer_size):
    if sub_cmd == SUB_S_MONITOR_ITEMS:
        server_list = MonitorCMD.CMD_MONITOR_ITEM_LST()
        protocol_buffer = msg[10:10 + buffer_size]
        server_list.ParseFromString(protocol_buffer)

        thread3 = threading.Thread(target=open_ui, args=(server_list.items,))
        thread3.start()
        print("-------连接已成功！---------")
        print("更新列表！")

    elif sub_cmd == SUB_S_MONITOR_KEEPLIVE:  # 心跳包收到
        pass
    elif sub_cmd == SUB_S_MONITOR_STATE:  # 更新状态
        server_update = MonitorCMD.CMD_MONITOR_ITEM_STATE()
        protocol_buffer = msg[10:10 + buffer_size]
        # print(protocol_buffer)
        server_update.ParseFromString(protocol_buffer)
        print("更新状态！")
        # print(server_update)
        refresh_server_list_info(server_update)      # 把数据传给界面显示
    elif sub_cmd == SUB_S_NEW_MONITOR_ITEM:
        # 新增加了一个服务器
        server_add = MonitorCMD.CMD_MONITOR_NEW_ITEM()
        protocol_buffer = msg[10:10 + buffer_size]
        # print(protocol_buffer)
        server_add.ParseFromString(protocol_buffer)
        print("新增一个服务器！")
        # print(server_add)
        add_server_list(server_add)  # 把数据传给界面显示

    elif sub_cmd == SUB_S_DEL_MONITOR_ITEM:
        # 删除了一个服务器
        server_del = MonitorCMD.CMD_MONITOR_DEL_ITEM()
        protocol_buffer = msg[10:10 + buffer_size]
        # print(protocol_buffer)
        server_del.ParseFromString(protocol_buffer)
        print("删除一个服务器！")
        del_server_list(server_del)  # 把数据传给界面显示

    elif sub_cmd == SUB_S_MONITOR_CMD:
        print("执行命令回复")
        gm_cmd = MonitorCMD.CMD_MONITOR_CMD_RESP()
        protocol_buffer = msg[10:10 + buffer_size]
        # print(protocol_buffer)
        gm_cmd.ParseFromString(protocol_buffer)
        print(gm_cmd)



def recv_loop(s):
    while True:
        msg = s.recv(1024 * 8)  # 接收字节的数据
        # print(msg)
        sub_cmd, buffer_size = deal_recv_tcp_deader_data(msg)
        deal_recv_protocol_data(sub_cmd, msg, buffer_size)
        time.sleep(0.2)

def send_loop(s):
    while True:
        # 发送心跳包
        s.send(get_send_tcp_header_data(MAIN_CMD_ID, SUB_C_MONITOR_KEEPLIVE, 0))  # 发送注册客户端消息给日志服务器
        time.sleep(1)

# 组合成数据包头部
def get_send_tcp_header_data(maincmd, childcmd, size):
    buffer_t = struct.pack("BBHHHH", 0, 1, size, maincmd, childcmd, 0)
    print(buffer_t)
    return buffer_t


s = None
def get_socket():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = socket.gethostname()

    conf = iniparser.INIParser()
    conf.read("Setting.ini")
    root = conf.get_section("author")
    host = root.get("ServerIP")
    port = root.get_int("port")

    s.connect((host, port))
    return s
def main():
    print("---------start!---------")

    s = get_socket()
    s.send(get_send_tcp_header_data(MAIN_CMD_ID, SUB_C_MONITOR_REG, 0))  # 发送注册客户端消息给日志服务器

    thread1 = threading.Thread(target=recv_loop, args=(s,))
    thread1.start()

    thread2 = threading.Thread(target=send_loop, args=(s,))
    thread2.start()

    # s.close()

    # print("---------end!---------")



if __name__ == "__main__":
    main()



def send_gm_cmd(server_id, cmd):
    send_cmd = MonitorCMD.CMD_MONITOR_CMD()
    send_cmd.server_id = int(server_id)
    send_cmd.cmd = cmd.encode(encoding="gb2312")
    # print(send_cmd)
    buffer_cmd = send_cmd.SerializeToString()
    # print(buffer_cmd)

    size = len(buffer_cmd)
    buffer_t = get_send_tcp_header_data(MAIN_CMD_ID, SUB_C_MONITOR_CMD, size)
    # print(buffer_t)

    # print(buffer_t + buffer_cmd)
    s = get_socket()
    s.send(buffer_t + buffer_cmd)  # 发送注册客户端消息给日志服务器
    # print('send gm cmd')
