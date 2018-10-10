# -*- coding: UTF-8 -*-
import hashlib

import core
from Action import *
from core.ClientSession import *
from protocal.CMD_Common_pb2 import *
from protocal.CMD_GlobalServer_pb2 import *
from protocal.protocol_cs import *
from protocal.protocol_ls import *
from protocal.protocol_gs import *
from protocal.CMD_LoginServer_pb2 import *
from protocal.CMD_GameServer_pb2 import *
from protocal.CMD_Game_pb2 import *

# client 显示的最大消息数量
MAX_LOG_COUNT = 60
# client 最多保存10条鱼
MAX_FISH_CNT = 20


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


# 客户端状态
class ClientState(object):
    none = 0
    connecting_ls = 1  # 正在连接登录服务器
    connected_ls = 2  # 已连接登录服务器
    logining = 3  # 正在登录
    logined = 4  # 已登录
    login_failed = 5  # 登录失败
    connecting_gs = 6  # 正在连接gameserver
    connected_gs = 7  # 已连接gameserver
    logining_gs = 8  # 正在登录gameserver
    logined_gs = 9  # 已登录gameserver
    login_failed_gs = 10  # 登录失败gameserver
    entering = 11  # 正在进入场景
    entered = 12  # 已进入场景
    playing = 13  # 正在游戏
    connecting_cs = 14  # 正在连接chatserver
    connected_cs = 15  # 已连接chatserver
    logining_cs = 16  # 正在登录chatserver
    logined_cs = 17  # 已登录chatserver
    login_failed_cs = 18  # 已登录chatserver
    die = 19  # 已异常断开


# 鱼过期时间,默认30秒
FISH_OVERDURE_TIME = 10

g_user_ids = []


# 机器人客户端对象
class Client(object):
    MAX_USER_ID = 0

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

    def connect_login_server(self, ip, port):
        self.client_state = ClientState.connecting_ls
        self.client_session.connect_login_server(ip, port)

    def on_loginsvr_connect(self):
        self.client_state = ClientState.connected_ls

    def connect_game_server(self, ip, port):
        self.client_state = ClientState.connecting_gs
        self.client_session.connect_game_server(ip, port)

    def on_gamesvr_connect(self):
        self.client_state = ClientState.connected_gs

    def connect_chat_server(self, ip, port):
        self.client_state = ClientState.connecting_cs
        self.client_session.connect_chat_server(ip, port)

    def on_chatsvr_connect(self):
        self.client_state = ClientState.connected_cs

    def log(self, msg):
        # print(msg.decode('utf-8').encode('gb2312'))
        print(msg)
        # print msg
        return
        self.log_list.append(msg)
        if len(self.log_list) > MAX_LOG_COUNT:
            self.log_list.pop(0)

    def print_log(self):
        for log in self.log_list:
            print log

    # 删除过期的鱼
    def check_overdue_fish(self):
        time_now = time.time()
        fishs = self.fish_pool.values()
        for fish in fishs:
            if time_now > fish.tick + FISH_OVERDURE_TIME:
                del self.fish_pool[fish.uid]

    # 逻辑处理
    def update(self):
        b_ai_ok = False
        if self.ai_action is not None and self.ai_action.is_valid():
            b_ai_ok = True

        # 处理接收的消息
        while self.client_session.recv_msg_queue.size() > 0:
            msg = self.client_session.recv_msg_queue.pop()
            if msg is not None:
                b_handle_ok = self.handle_net_msg(msg)
                if b_ai_ok and not b_handle_ok:
                    self.ai_action.handle_net_msg(msg)

        # 更新Ai状态
        time_now = time.time()
        if self.ai_action is not None and self.ai_action.is_valid():
            if time_now > self.last_ai_update_tick + 0.2:
                self.last_ai_update_tick = time_now
                if self.client_state != ClientState.connecting_gs:
                    self.ai_action.update()

        # 处理过期的鱼
        if time_now > self.last_check_due_tick + 1 and len(self.fish_pool) > 0:
            self.last_check_due_tick = time_now
            self.check_overdue_fish()

    # 登录
    def login(self):
        cmd = CMD_MB_GuestLogin()
        cmd.machine_id = self.guest_info.machine_id
        cmd.ditch_number = self.guest_info.ditch_id
        cmd.client_kind = self.guest_info.client_kind
        cmd.game_kind_id = self.guest_info.game_kind
        cmd.plaza_version = self.guest_info.client_version
        cmd.ip_addr = self.guest_info.ip_address
        cmd.device_type = self.guest_info.device_type
        s = cmd.SerializeToString()
        self.client_state = ClientState.logining
        self.client_session.send_data(MDM_MB_LOGON, SUB_MB_GUESTLOGIN, s)

    # 登录成功
    def handle_login_sucess(self, data):
        msg = CMD_MB_LogonSuccess()
        msg.ParseFromString(data)
        self.role_base_info.face_id = msg.face_id
        self.role_base_info.gender = msg.gender
        self.role_base_info.user_id = msg.user_id
        self.role_base_info.game_id = msg.game_id
        self.role_base_info.exp = msg.exp
        self.role_base_info.loveliness = msg.love_liness
        self.role_base_info.score = msg.user_score
        self.role_base_info.nick_name = msg.nick_name
        self.role_base_info.level = msg.level
        self.role_base_info.vip_level = msg.vip_lev
        self.role_base_info.account_level = msg.account_level
        self.role_base_info.site_level = msg.sitelevel
        self.role_base_info.cur_level_exp = msg.cur_level_exp
        self.role_base_info.next_level_exp = msg.next_level_exp
        self.role_base_info.pay_total = msg.pay_total
        self.role_base_info.diamond = msg.user_diamond
        g_user_ids.append(msg.user_id)

        if Client.MAX_USER_ID < msg.user_id:
            Client.MAX_USER_ID = msg.user_id

        # 生成游客登录密码(gs)
        blanks = []
        cnt = 32 - len(self.guest_info.machine_id)
        if cnt > 0:
            for i in range(cnt):
                blanks.append(' ')
        temp = self.guest_info.machine_id + ''.join(blanks) + str(msg.user_id)
        uni_str = temp.decode('utf-8')
        buf = ''
        for e in uni_str:
            buf += struct.pack('H', ord(e))
        md = hashlib.md5()
        md.update(buf)
        self.login_passwd = str(md.hexdigest()).upper()

    def handle_cs_info(self, data):
        msg = CMD_S_CHAT_SERVER_INFO()
        msg.ParseFromString(data)
        self.chat_server_ip = msg.addr
        self.chat_server_port = msg.port
        self.chat_token = msg.token
        self.chat_rand = msg.rand
        self.client_state = ClientState.logined

    # 登录失败
    def handle_login_failed(self, data):
        msg = CMD_MB_LogonFailure()
        msg.ParseFromString(data)
        self.client_state = ClientState.login_failed
        self.log("guest login failed:%s" % msg.describe)

    # 登录成功后下发服务器列表
    def handle_server_list(self, data):
        msg = CMD_MB_LIST_SERVER()
        msg.ParseFromString(data)
        for item in msg.game_server_list:
            info = GameServerInfo()
            info.kind_id = item.kind_id
            info.node_id = item.node_id
            info.sort_id = item.sort_id
            info.server_id = item.server_id
            info.server_port = item.server_port
            info.online_count = item.online_count
            info.online_pc = item.online_pc
            info.online_andriod = item.online_andriod
            info.online_ios = item.online_ios
            info.full_count = item.full_count
            for arr in item.server_addr:
                info.server_addr.append(arr)
            info.server_name = item.server_name
            info.cell_score = item.cell_score
            info.min_enter_score = item.min_enter_score
            info.max_enter_score = item.max_enter_score
            info.server_type = item.server_type
            info.min_enter_vip = item.min_enter_vip
            info.min_enter_cannon_lev = item.min_enter_cannon_lev
            info.server_rule = item.server_rule
            self.gameserver_list.append(info)

    # 登录cs
    def login_cs(self):
        cmd = CMD_C_LOGIN()
        cmd.user_id = self.role_base_info.user_id
        cmd.game_id = self.role_base_info.game_id
        cmd.token = self.chat_token
        s = cmd.SerializeToString()
        self.client_state = ClientState.logining_cs
        self.client_session.send_data(MAIN_CHAT_CMD, SUB_C_LOGIN, s)

    def handle_login_cs(self, data):
        msg = CMD_S_LOGIN()
        msg.ParseFromString(data)
        if msg.result == Successful:
            self.client_state = ClientState.logined_cs
        else:
            self.client_state = ClientState.login_failed_cs

    def add_friend(self, userid):
        if userid in self.friend_set:
            return
        self.friend_list.append(userid)
        self.friend_set = set(self.friend_list)

        if self.role_base_info.user_id == userid:
            self.log("add friend error! add self! %d" % userid)
            return
        self.log("add friend: %d" % userid)

    def random_stranger(self):
        if len(g_user_ids) == 0:
            return 0
        user_id = g_user_ids[random.randint(0, len(g_user_ids) - 1)]
        if user_id == self.role_base_info.user_id:
            return 0

        if user_id in self.friend_set:
            return 0
        return user_id

    def random_friend(self):
        if len(self.friend_list) == 0:
            return 0
        user_id = self.friend_list[random.randint(0, len(self.friend_list) - 1)]
        return user_id

    # 登录gs
    def login_gs(self):
        cmd = CMD_GR_LogonUserID()
        cmd.plaza_version = self.guest_info.client_version
        cmd.frame_version = 101056515
        cmd.process_version = 101056515
        cmd.client_type = self.guest_info.client_type
        cmd.user_id = self.role_base_info.user_id
        cmd.password = self.login_passwd
        cmd.machine_id = self.guest_info.machine_id
        cmd.kind_id = self.guest_info.client_kind
        cmd.ip_addr = self.guest_info.ip_address
        cmd.ditch_number = self.guest_info.ditch_id
        cmd.device_type = self.guest_info.device_type
        cmd.packet_index = 1
        cmd.is_android = 0
        cmd.cannon_mulriple = 0

        s = cmd.SerializeToString()
        self.client_state = ClientState.logining_gs
        self.client_session.send_data(MDM_GR_LOGON, SUB_GR_LOGON_USERID, s)

    # gs 登录成功
    def handle_login_sucess_gs(self, data):
        msg = CMD_GR_LogonSuccess()
        msg.ParseFromString(data)
        self.client_state = ClientState.logined_gs

    # gs 登录失败
    def handle_login_failed_gs(self, data):
        msg = CMD_GR_LogonFailure()
        msg.ParseFromString(data)
        self.client_state = ClientState.login_failed_gs
        self.log("login gs failed:%s" % msg.describe)

    def enter_scence(self):
        cmd = CMD_GF_GameOption()
        cmd.allow_lookon = 0
        cmd.frame_version = 0
        cmd.client_version = 0
        s = cmd.SerializeToString()
        self.client_state = ClientState.entering
        self.client_session.send_data(MDM_GF_FRAME, SUB_GF_GAME_OPTION, s)

    # 更新游戏状态
    def handle_game_status(self, data):
        msg = CMD_GF_GameStatus()
        msg.ParseFromString(data)
        pass

    def handle_game_message(self, data):
        msg = CMD_CR_SystemMessage()
        msg.ParseFromString(data)
        self.log("消息:" + msg.text)
        if msg.text.find("欢迎您进入") != -1:
            self.client_state = ClientState.entered

    # 接收技能
    def handle_user_skill(self, data):
        msg = CMD_CF_S_UserSkill()
        msg.ParseFromString(data)

    # 自己进入房间
    def handle_enter_scence(self, data):
        msg = CMD_S_ENTER_SCENE()
        msg.ParseFromString(data)
        for user in msg.table_users:
            if user.user_id == self.role_base_info.user_id:
                self.chair_id = user.chair_id
        self.client_state = ClientState.entered
        self.log("进入场景,场景id:%d,桌子id:%d,椅子id:%d" % (msg.scene_id, msg.table_id, self.chair_id))

    # 其他人进入房间
    def handle_other_enter_scence(self, data):
        msg = CMD_S_OTHER_ENTER_SCENE()
        msg.ParseFromString(data)
        try:
            self.log("%s 进入了房间" + msg.user_info.nick_name())
        except Exception, e:
            pass

    # 场景鱼刷新
    def handle_scene_fish(self, data):
        fish_cnt = len(self.fish_pool)
        if fish_cnt > MAX_FISH_CNT:
            return

        msg = CMD_S_SCENE_FISH()
        msg.ParseFromString(data)
        for fish in msg.scene_fishs:
            info = FishObj()
            info.uid = fish.uid
            info.kind_id = fish.kind_id
            info.tick = time.time()
            self.fish_pool[info.uid] = info
            fish_cnt += 1
            if fish_cnt > MAX_FISH_CNT:
                return

    # 新增鱼
    def handle_new_fish(self, data):
        fish_cnt = len(self.fish_pool)
        if fish_cnt > MAX_FISH_CNT:
            return

        msg = CMD_S_DISTRIBUTE_FISH()
        msg.ParseFromString(data)
        for fish in msg.fishs:
            info = FishObj()
            info.uid = fish.uid
            info.kind_id = fish.kind_id
            info.tick = time.time()
            self.fish_pool[info.uid] = info
            fish_cnt += 1
            if fish_cnt > MAX_FISH_CNT:
                return

    # 网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id
        b_handle_ok = True
        # self.log("handle net msg:%d,%d" % (msg_id, sub_msg_id))
        # -----------------loginserver msg-----------------
        if msg_id == MDM_MB_LOGON:
            if sub_msg_id == SUB_MB_LOGON_SUCCESS:
                self.handle_login_sucess(msg.data)
            elif sub_msg_id == SUB_MB_LOGON_FAILURE:
                self.handle_login_failed(msg.data)
            elif sub_msg_id == SUB_MB_LOGON_FINISH:
                pass
            else:
                b_handle_ok = False
        elif msg_id == MDM_MB_GIFT_PACK:
            if sub_msg_id == SUB_MB_L2C_GIFT_PRODUCT_INFO:
                pass  # 礼包
            else:
                b_handle_ok = False
        elif msg_id == MDM_MB_ACTIVITY:
            if sub_msg_id == SUB_MB_S2C_ACTIVITY:
                pass  # 活动
            elif sub_msg_id == SUB_MB_S2C_ACTIVITY_CELL_INFO_LIST:
                pass  # 活动
            else:
                b_handle_ok = False
        elif msg_id == MAIN_CHAT_CMD:
            if sub_msg_id == SUB_S_LOGIN:
                self.handle_login_cs(msg.data)
            else:
                b_handle_ok = False
        elif msg_id == MDM_MB_VIP:
            if sub_msg_id == SUB_MB_S_VIP_INFO:
                pass  # vip 信息
        elif msg_id == MDM_MB_SERVER_LIST:
            if sub_msg_id == SUB_MB_LIST_SERVER:
                self.handle_server_list(msg.data)
            elif sub_msg_id == SUB_MB_LIST_FINISH:
                pass  # 房间信息完成
            else:
                b_handle_ok = False
        elif msg_id == MDM_MB_USER_INFO:
            if sub_msg_id == SUB_MB_S_GET_CHAT_SERVER_INFO:
                self.handle_cs_info(msg.data)
            if sub_msg_id == SUB_MB_S_USER_MATERIAL_OBJECT:
                pass  # 玩家信息
            if sub_msg_id == SUB_MB_S_REQUEST_ARENA:
                pass  # 竞技场数据
            else:
                b_handle_ok = False
        # -----------------gameserver msg-----------------
        elif msg_id == MDM_GR_LOGON:
            if sub_msg_id == SUB_GR_LOGON_FAILURE:
                self.handle_login_failed_gs(msg.data)
            elif sub_msg_id == SUB_GR_LOGON_SUCCESS:
                self.handle_login_sucess_gs(msg.data)
            elif sub_msg_id == SUB_GR_LOGON_FINISH:
                pass  # gs 登录完成
            else:
                b_handle_ok = False
        # -----------------游戏场景 msg-----------------
        elif msg_id == MDM_GF_FRAME:
            if sub_msg_id == SUB_GF_GAME_STATUS:
                self.handle_game_status(msg.data)
            elif sub_msg_id == SUB_GF_SYSTEM_MESSAGE:
                self.handle_game_message(msg.data)
            elif sub_msg_id == SUB_GF_USER_SKILL:
                self.handle_user_skill(msg.data)
            else:
                b_handle_ok = False
        # -----------------场景内 msg-----------------
        elif msg_id == MDM_GF_GAME:
            if sub_msg_id == SUB_S_ENTER_SCENE:
                self.handle_enter_scence(msg.data)
            elif sub_msg_id == SUB_S_OTHER_ENTER_SCENE:
                self.handle_other_enter_scence(msg.data)
                # 进入场景,接收鱼数据
            elif sub_msg_id == SUB_S_SCENE_FISH:
                self.handle_scene_fish(msg.data)
                # 新生成鱼
            elif sub_msg_id == SUB_S_DISTRIBUTE_FISH:
                self.handle_new_fish(msg.data)
            else:
                b_handle_ok = False
        else:
            b_handle_ok = False

        return b_handle_ok
