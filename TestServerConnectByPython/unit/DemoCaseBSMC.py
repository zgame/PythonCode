# -*- coding: UTF-8 -*-
from core.ActionGM import *
from protocal.CMD_BSMC_Game_pb2 import *
from protocal.protocol_bsmc import *
from protocal.protocol_gs import *
from unit.BaseCase import BaseCase

# 本测试用例主要用于统计各种概率的分数分布情况

if True:
    LOGIN_SERVER_IP = '192.168.101.85'
    LOGIN_SERVER_PORT = 8300
else:
    LOGIN_SERVER_IP = '192.168.0.218'
    LOGIN_SERVER_PORT = 8600

# 机器人数
ROBOT_COUNT = 100
# 下注间隔
BET_CD = 3

# 测试初始金币
INIT_SCORE = 5000000
# 测试
INIT_TOTAL_PAY = 5000
# 初始充值贡献
INIT_PAY_CONTRIBUTE = 5000000
# 测试起始杀分游戏赞助值
INIT_KILL_AID = 50000000
# 测试起始杀分大奖额度
INIT_KILL_USEABLE = 50000000
# 设置起始大奖池数量
INIT_PRIZE_POOL = 50000000000


# 统计信息
class StatInfo(object):
    def __init__(self):
        self.nSize = 4
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
        elif score < 1000:
            self.nCnt0_1000 += 1
        elif score <= 10000:
            self.nCnt1000_10000 += 1
        elif score <= 15000:
            self.nCnt10000_15000 += 1
        elif score < 50000:
            self.nCnt15000_50000 += 1
        else:
            self.nCnt50000_ += 1

        if self.nCurTime == 2000000:
            self.dum_stat_info()
            self.bNeedRun = False
        elif self.nCurTime % 100 == 0:
            print ("-----------------run :%d------------------------" % self.nCurTime)

    def dum_stat_info(self):
        print (
        "--尺寸:%d x %d, 次数:%d, 总得分:%d, 0消除:%d, (0,1000]:%d,(1000,10000]:%d,(10000,15000]:%d,(15000,50000]:%d,(50000,+]:%d --" % (
            self.nSize, self.nSize, 10000, self.llScore, self.nCnt0, self.nCnt0_1000, self.nCnt1000_10000,
            self.nCnt10000_15000, self.nCnt15000_50000, self.nCnt50000_))

        print ("")
        print ("")
        print ("-------------------------分数分布----------------------------------")
        for K, V in self._dict.items():
            print ("    %10d:   %d" % (K, V))
        print ("-------------------------stat info end-----------------------------")


G_Stat = StatInfo()

# 玩游戏
class PlayActionBSMC(BaseAction):
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
        if super(PlayActionBSMC, self).update():
            return True

        self.do_play()
        return False

    def do_bet(self):
        cmd = CMD_SUB_C_BET()
        cmd.bet_score = 50000
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MDM_GF_GAME, SUB_C_BET, s)

    def do_award(self):
        cmd = CMD_SUB_C_AWARD()
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MDM_GF_GAME, SUB_C_GET_AWARD, s)

    # 模拟游戏逻辑
    def do_play(self):
        tm_now = time.time()
        if tm_now > self.last_bet_tick + self.bet_cd:
            self.last_bet_tick = tm_now
            if G_Stat.is_need_run():
                self.do_bet()

    # 处理赌博结果
    def handle_bet_result(self, data):
        msg = CMD_SUB_S_BET()
        msg.ParseFromString(data)
        if msg.result:
            G_Stat.add_score(msg.data.get_score)
            self.client.log(
                "%d x %d 下注:%d,获得:%d" % (msg.data.size, msg.data.size, msg.data.bet_score, msg.data.get_score))
        else:
            if msg.err_msg.find("已通关") == 0:
                self.do_award()
            else:
                self.client.log(msg.err_msg)

    # 处理网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id

        if msg_id == MDM_GF_GAME:
            if sub_msg_id == SUB_S_BET:
                self.handle_bet_result(msg.data)


# 宝石迷城演示用测试用例
class DemoCaseBSMC(BaseCase):
    def __init__(self):
        self.mac_start_idx = 158654493214311 + random.randint(0, 100000)  # my real mac 74-D4-35-B8-F8-B8
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        super(DemoCaseBSMC, self).__init__()

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
        ai_list = super(DemoCaseBSMC, self).build_ai(client)
        # 配置登录服务器
        connect_action = ConnectLsAction(client)
        connect_action.server_ip = LOGIN_SERVER_IP
        connect_action.server_port = LOGIN_SERVER_PORT
        ai_list.add_action(connect_action)
        # 登录
        ai_list.add_action(LoginAction(client))
        ai_list.add_action(ConnectGsAction(client))
        ai_list.add_action(LoginGSAction(client))
        # ai_list.add_action(GMCMDOnceAction(client, "@设置游戏大奖池 %d" % INIT_PRIZE_POOL))
        ai_list.add_action(GMCMDAction(client, "@设置金币 %d" % INIT_SCORE))
        ai_list.add_action(GMCMDAction(client, "@设置充值总额 %d" % INIT_TOTAL_PAY))
        ai_list.add_action(GMCMDAction(client, "@设置充值贡献 %d" % INIT_PAY_CONTRIBUTE))
        ai_list.add_action(EnterScenceAction(client))
        ai_list.add_action(PlayActionBSMC(client))
        return ai_list
