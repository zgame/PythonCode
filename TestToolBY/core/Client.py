# -*- coding: UTF-8 -*-
from core.ClientSession import *
import protocal.cmd_common as Cmd
from protocal.cmd_common_pb2 import *


# client 显示的最大消息数量
MAX_LOG_COUNT = 60


# 角色基本信息
class RoleBaseInfo(object):
    def __init__(self):
        self.face_id = 0  # 头像id
        self.gender = 0  # 性别
        self.user_id = 0  # 用户id
        self.game_id = 0  # 游戏id
        self.exp = 0  # 经验
        self.loveliness = 0  # 魅力
        self.score = 0  # 分数
        self.nick_name = ''  # 昵称
        self.level = 0  # 等级
        self.vip_level = 0  # vip等级
        self.account_level = 0  # 账号等级
        self.site_level = 0  # 炮等级
        self.cur_level_exp = 0  # 当前等级经验
        self.next_level_exp = 0  # 下一等级经验
        self.pay_total = 0  # 充值总金额
        self.diamond = 0  # 钻石数量
        self.fire_cnt = 0 # 开炮次数


# 客户端状态
class ClientState(object):
    none = 0
    connecting = 1  # 正在连接登录服务器
    connected = 2  # 已连接登录服务器
    connect_failed = 3 # 连接失败
    logining = 4  # 正在登录
    logined = 5  # 已登录
    login_failed = 6  # 登录失败
    entering = 7  # 正在进入场景
    entered = 8  # 已进入场景
    playing = 9  # 正在游戏


# 鱼过期时间,默认30秒
FISH_OVERDURE_TIME = 30

g_user_ids = []


# 机器人客户端对象
class Client(object):
    def __init__(self):
        # 基本角色数据
        self.role_base_info = RoleBaseInfo()
        # 设备信息
        self.guest_info = GuestInfo()
        # 状态
        self.client_state = ClientState.none
        # 消息列表
        self.log_list = []
        # 测试ai
        self.ai_action = None
        # session 对象
        self.client_session = G_SessionMgr.new_session()
        self.client_session.client = self
        # gameserver列表
        self.gameserver_list = []
        # 登录密码
        self.login_passwd = ''
        # 场景中的鱼
        self.fish_pool = {}
        # 检查鱼过期
        self.last_check_due_tick = 0
        # ai更新时间
        self.last_ai_update_tick = 0
        # 椅子id
        self.chair_id = 0
        # 发射炮弹数量
        self.fire_cnt = 0
        # 捕获鱼的数量
        self.catch_cnt = 0
        # 聊天服务器ip
        self.chat_server_ip = ''
        # 聊天服务器端口
        self.chat_server_port = 0
        # 聊天服务器token
        self.chat_token = ''
        # 聊天服务器rand
        self.chat_rand = 0
        # 好友列表
        self.friend_list = []
        self.friend_set = set()

    def change_state(self, state):
        self.client_state = state

    def connect_server(self, ip, port):
        self.change_state(ClientState.connecting)
        self.client_session.connect_server(ip, port)

    def on_connect(self):
        self.change_state(ClientState.connected)

    def on_connect_failed(self):
        self.change_state(ClientState.connect_failed)

    def log(self, msg):
        print msg
        return
        self.log_list.append(msg)
        if len(self.log_list) > MAX_LOG_COUNT:
            self.log_list.pop(0)

    def print_log(self):
        for log in self.log_list:
            print log

    # 逻辑处理
    def update(self):
        # 处理接收的消息
        msg = self.client_session.recv_msg_queue.pop()
        if msg is not None:
            self.handle_net_msg(msg)

        # 更新Ai状态
        time_now = time.time()
        if self.ai_action is not None and self.ai_action.is_valid():
            if time_now > self.last_ai_update_tick + 0.2:
                self.last_ai_update_tick = time_now
                self.ai_action.update()
            if msg is not None:
                self.ai_action.handle_net_msg(msg)

        # 处理过期的鱼
        if len(self.fish_pool) > 0 and time_now > self.last_check_due_tick + 1:
            self.last_check_due_tick = time_now
            self.check_overdue_fish()

    # 登录
    def login(self):
        cmd = cmd_client_login()
        cmd.user_id = self.guest_info.user_id
        cmd.mac_id = self.guest_info.machine_id
        cmd.game_kind = self.guest_info.game_kind
        cmd.plat_kind = self.guest_info.plat_kind
        cmd.client_ver = self.guest_info.client_version
        cmd.client_ip = self.guest_info.ip_address
        cmd.client_type = self.guest_info.client_type
        cmd.device_type = self.guest_info.device_type
        cmd.ditch_id = self.guest_info.ditch_id
        s = cmd.SerializeToString()
        self.change_state(ClientState.logining)
        self.client_session.send_data(Cmd.COMMON, Cmd.COMMON_SUB_C_LOGIN, s)

    # 登录成功
    def handle_login_result(self, data):
        msg = cmd_client_login_rsp()
        msg.ParseFromString(data)
        self.log("登录返回, %d,%d,%d,%s" % (msg.user_id, msg.game_id, msg.coin, msg.nick_name))
        if msg.error_msg is None or msg.error_msg == '':
            self.role_base_info.user_id = msg.user_id
            self.role_base_info.game_id = msg.game_id
            self.role_base_info.score = msg.coin
            self.role_base_info.nick_name = msg.nick_name
            g_user_ids.append(msg.user_id)
            self.change_state(ClientState.logined)
        else:
            self.change_state(ClientState.login_failed)
            self.log("登录失败:%s" % msg.error_msg)

    # 金币变更
    def handle_coin_change(self, data):
        msg = cmd_coin_chg()
        msg.ParseFromString(data)
        self.role_base_info.score += msg.change
        if msg.change > 0:
            self.log("元宝增加:%f" % msg.change)
        else:
            self.log("元宝减少:%f" % -msg.change)

    # 网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id
        # self.log("handle net msg:%d,%d" % (msg_id, sub_msg_id))
        # -----------------common msg-----------------
        if msg_id == Cmd.COMMON:
            if sub_msg_id == Cmd.COMMON_SUB_S_LOGIN:
                self.handle_login_result(msg.data)
            elif sub_msg_id == Cmd.COMMON_SUB_S_COINCHG:
                self.handle_coin_change(msg.data)


# 假人对象管理器
class ClientManager(object):
    def __init__(self):
        # 机器人字典
        self.client_dict = {}

    # 添加一个测试机器人
    def add_client(self, client):
        if client is None:
            return
        self.client_dict[client.guest_info.user_id] = client

    def update(self):
        for client in self.client_dict.values():
            client.update()
