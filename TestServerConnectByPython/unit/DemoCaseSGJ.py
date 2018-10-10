# -*- coding: UTF-8 -*-
from core.Action import *
from core.ActionGM import *
from core.Client import *
from protocal.CMD_SGJ_Game_pb2 import *
from protocal.protocol_sgj import *
from unit.BaseCase import BaseCase

if True:
    LOGIN_SERVER_IP = '192.168.101.85'
    LOGIN_SERVER_PORT = 8300
else:
    LOGIN_SERVER_IP = '192.168.0.218'
    LOGIN_SERVER_PORT = 8600

# 机器人数
ROBOT_COUNT = 1
# 下注间隔
BET_CD = 3
# 水果机下注信息
# 第一个字段: 下注索引, 第二个字段: 下注分数, 第三个字段: 机器人作弊标记
BET_CHIP_ARR = [[3, 1000, 0], [1, 1000, 0]]


# 统计信息
class SGJ_StatInfo(object):
    def __init__(self):
        self.bNeedRun = True
        self.llScore = 0  # 总收益
        self.nCnt0 = 0  # 0消除次数
        self.nCnt0_1000 = 0  # 1~1000
        self.nCnt1000_10000 = 0
        self.nCnt10000_15000 = 0
        self.nCnt15000_50000 = 0
        self.nCnt50000_ = 0
        self.nCurTime = 0
        self._dict = {}

    def is_need_run(self):
        return self.bNeedRun

    def add_score(self, score):
        self.nCurTime += 1
        if self._dict.has_key(score):
            self._dict[score] += 1
        else:
            self._dict[score] = 1

        self.llScore += score

        if score == 0:
            self.nCnt0 += 1
        elif score <= 1000:
            self.nCnt0_1000 += 1
        elif score <= 10000:
            self.nCnt1000_10000 += 1
        elif score <= 15000:
            self.nCnt10000_15000 += 1
        elif score < 50000:
            self.nCnt15000_50000 += 1
        else:
            self.nCnt50000_ += 1

        if self.nCurTime == 10000:
            self.dum_stat_info()
            self.bNeedRun = False
        elif self.nCurTime % 100 == 0:
            print ("-----------------run :%d------------------------" % self.nCurTime)

    def dum_stat_info(self):
        print (
            "--水浒传下注次数:%d, 总得分:%d, 0消除:%d, (0,1000]:%d,(1000,10000]:%d,(10000,15000]:%d,(15000,50000]:%d,(50000,+]:%d --" % (
                10000, self.llScore, self.nCnt0, self.nCnt0_1000, self.nCnt1000_10000,
                self.nCnt10000_15000, self.nCnt15000_50000, self.nCnt50000_))

        print ("")
        print ("")
        print ("-------------------------分数分布----------------------------------")
        for K, V in self._dict.items():
            print ("    %10d:   %d" % (K, V))
        print ("-------------------------stat info end-----------------------------")


G_StatSGJ = SGJ_StatInfo()


# 玩游戏
class PlayActionSGJ(BaseAction):
    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '玩游戏'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务
        self.bet_cd = BET_CD  # 下注间隔
        self.last_bet_tick = 0  # 上次开炮时间

    def do(self):
        state = self.client.client_state
        if state == ClientState.entered:
            self.on_begin()
        else:
            self.on_failed("当前未进入场景 ?")

    def update(self):
        if super(PlayActionSGJ, self).update():
            return True

        self.do_play()
        return False

    def do_bet(self):
        # 下注
        for k in BET_CHIP_ARR:
            chip = CMD_UserChip_C()
            chip.chip_index = k[0]
            chip.chip_value = k[1]
            chip.android_cheat = k[2]
            s = chip.SerializeToString()
            self.client.client_session.send_data(MDM_GF_GAME, SUB_C_UserChip, s)

        # 开始
        cmd = CMD_StartGame_Single()
        cmd.user_cheat = False
        s2 = cmd.SerializeToString()
        self.client.client_session.send_data(MDM_GF_GAME, SUB_C_StartGame_Single, s2)

    # 模拟游戏逻辑
    def do_play(self):
        tm_now = time.time()
        if tm_now > self.last_bet_tick + self.bet_cd:
            self.last_bet_tick = tm_now
            if G_StatSGJ.is_need_run():
                self.do_bet()

    # 处理赌博结果
    def handle_bet_result(self, data):
        msg = CMD_GameResultinfo_S()
        msg.ParseFromString(data)
        G_StatSGJ.add_score(msg.win_score_change)
        self.client.log("下注:%d,获得:%d" % (msg.chip_value, msg.win_score_change))

    @staticmethod
    def handle_bet_error(data):
        msg = CMD_SysMessage_S()
        msg.ParseFromString(data)
        print(msg.sys_message)

    # 处理网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id

        if msg_id == MDM_GF_GAME:
            if sub_msg_id == SUB_S_GameResultInfo:
                self.handle_bet_result(msg.data)
            elif sub_msg_id == SUB_S_SysMessage:
                self.handle_bet_error(msg.data)


# 水浒传用测试用例
class DemoCaseSGJ(BaseCase):
    def __init__(self):
        self.mac_start_idx = 138624493214311 + random.randint(0, 100000)  # my real mac 74-D4-35-B8-F8-B8
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        super(DemoCaseSGJ, self).__init__()

    # 创建测试客户端对象
    def build_guest(self):
        for i in range(self.robot_cnt):
            guest = GuestInfo()
            guest.machine_id = build_mac_addr(self.mac_start_idx + i)
            guest.client_version = 0
            guest.ip_address = "192.168.102.23"
            guest.client_kind = 405
            self.guests.append(guest)

    def build_ai(self, client):
        ai_list = super(DemoCaseSGJ, self).build_ai(client)
        # 配置登录服务器
        connect_action = ConnectLsAction(client)
        connect_action.server_ip = LOGIN_SERVER_IP
        connect_action.server_port = LOGIN_SERVER_PORT
        ai_list.add_action(connect_action)
        # 登录
        ai_list.add_action(LoginAction(client))
        ai_list.add_action(ConnectGsAction(client))
        ai_list.add_action(LoginGSAction(client))
        ai_list.add_action(EnterScenceAction(client))
        ai_list.add_action(GMCMDAction(client, "@设置金币 500000"))
        ai_list.add_action(PlayActionSGJ(client))
        return ai_list
