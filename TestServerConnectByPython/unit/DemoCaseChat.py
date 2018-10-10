# -*- coding: UTF-8 -*-
from core.ActionGM import *
from unit.BaseCase import BaseCase

# 本测试用例主要测试聊天系统要情况

LOGIN_SERVER_IP = '192.168.101.72'
LOGIN_SERVER_PORT = 8300
CHAT_CD = 5
ADD_FRIEND_CD = 5
SEARCH_USER_CD = 5
ROBOT_COUNT = 500

alpha_arr = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def rand_str(strlen):
    str = []
    arr_len = len(alpha_arr)
    for i in range(0, strlen):
        str.append(alpha_arr[random.randint(1, arr_len - 1)])
    return "".join(str)


# 玩游戏
class ChatSysAction(BaseAction):
    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '聊天系统测试'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务
        self.last_chat_tick = 0
        self.last_add_tick = 0

    def do(self):
        state = self.client.client_state
        if state == ClientState.logined_cs:
            self.on_begin()
        else:
            self.on_failed("当前未连接聊天服务器 ?")

    def update(self):
        if super(ChatSysAction, self).update():
            return True

        self.do_play()
        return False

    def do_chat(self, user_id):
        if user_id == 0:
            return
        cmd = CMD_C_CHAT_MESSAGE()
        cmd.speaker_user_id = self.client.role_base_info.user_id
        cmd.friend_user_id = user_id
        cmd.msg = rand_str(random.randint(20, 50))
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MAIN_CHAT_CMD, SUB_C_CHAT_MESSAGE, s)

    def do_play(self):
        tm_now = time.time()
        if tm_now > self.last_chat_tick + CHAT_CD:
            self.last_chat_tick = tm_now
            self.do_chat(self.client.random_friend())
        if tm_now > self.last_add_tick + ADD_FRIEND_CD:
            self.last_add_tick = tm_now
            self.do_add_friend(self.client.random_stranger())

    # 添加好友
    def do_add_friend(self, userid):
        if userid == 0:
            return

        cmd = CMD_C_APPLY_FRIEND()
        cmd.apply.apply_id = self.client.role_base_info.user_id
        cmd.apply.be_applied_id = userid
        cmd.apply.opt = Apply
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MAIN_CHAT_CMD, SUB_C_APPLY_FRIEND, s)

    # 处理搜索结果
    def handle_search_result(self, data):
        msg = CMD_S_SEARCH_FRIEND()
        msg.ParseFromString(data)

    def handle_chat_result(self, data):
        msg = CMD_S_CHAT_MESSAGE()
        msg.ParseFromString(data)
        self.client.log("recv from: %d,msg:%s" % (msg.speaker_user_id, msg.msg.msg.decode('utf-8')))

    # 处理添加结果
    def handle_apply_result(self, data):
        msg = CMD_S_APPLY_FRIEND_RESULT()
        msg.ParseFromString(data)
        if msg.apply.opt == Apply:
            cmd = CMD_C_APPLY_FRIEND()
            if msg.apply.be_applied_id == self.client.role_base_info.user_id:
                cmd.apply.apply_id = msg.apply.apply_id
                cmd.apply.be_applied_id = msg.apply.be_applied_id
                cmd.apply.opt = Agree
                s = cmd.SerializeToString()
                self.client.client_session.send_data(MAIN_CHAT_CMD, SUB_C_APPLY_FRIEND, s)
            return
        if msg.apply.opt == Agree:
            if msg.apply.be_applied_id == self.client.role_base_info.user_id:
                self.client.add_friend(msg.apply.apply_id)
            else:
                self.client.add_friend(msg.apply.be_applied_id)
            return

    # 处理网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id

        if msg_id == MAIN_CHAT_CMD:
            if sub_msg_id == SUB_S_SEARCH_USER:
                self.handle_search_result(msg.data)
            if sub_msg_id == SUB_S_APPLY_FRIEND_RESULT:
                self.handle_apply_result(msg.data)
            if sub_msg_id == SUB_S_CHAT_MESSAGE:
                self.handle_chat_result(msg.data)


class GetChatServerInfo(BaseAction):
    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '获取聊天服信息'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        cmd = CMD_C_CHAT_SERVER_INFO()
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MDM_MB_USER_INFO, SUB_MB_C_GET_CHAT_SERVER_INFO, s)
        self.state = ActionState.doing

    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id
        if msg_id == MDM_MB_USER_INFO:
            if sub_msg_id == SUB_MB_S_GET_CHAT_SERVER_INFO:
                self.client.handle_cs_info(msg.data)
                self.state = ActionState.success

# 宝石迷城演示用测试用例
class DemoCaseChat(BaseCase):
    def __init__(self):
        self.mac_start_idx = 158654493214311 + random.randint(0, 100000)  # my real mac 74-D4-35-B8-F8-B8
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        super(DemoCaseChat, self).__init__()

    # 创建测试客户端对象
    def build_guest(self):
        for i in range(self.robot_cnt):
            guest = GuestInfo()
            guest.machine_id = build_mac_addr(self.mac_start_idx + i)
            guest.client_version = 0
            guest.ip_address = "192.168.102.23"
            guest.client_kind = 502
            self.guests.append(guest)

    def build_ai(self, client):
        ai_list = super(DemoCaseChat, self).build_ai(client)
        # 配置登录服务器
        connect_action = ConnectLsAction(client)
        connect_action.server_ip = LOGIN_SERVER_IP
        connect_action.server_port = LOGIN_SERVER_PORT
        ai_list.add_action(connect_action)
        # 登录
        ai_list.add_action(LoginAction(client))

        ai_list.add_action(ConnectChatAction(client))
        ai_list.add_action(LoginChatAction(client))
        ai_list.add_action(ChatSysAction(client))
        return ai_list


g_case_chat = DemoCaseChat()