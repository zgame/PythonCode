# -*- coding: UTF-8 -*-
from core.Action import *
from core.ActionGM import GMCMDAction
from protocal.CMD_SHZ_Game_pb2 import *
from protocal.protocol_shz import *
from unit.BaseCase import BaseCase

if True:
    LOGIN_SERVER_IP = '192.168.101.85'
    LOGIN_SERVER_PORT = 8300
else:
    LOGIN_SERVER_IP = '192.168.0.218'
    LOGIN_SERVER_PORT = 8600

# 机器人数
ROBOT_COUNT = 200
# 下注间隔
BET_CD = 2


# 统计信息
class SHZ_StatInfo(object):
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

        if self.nCurTime == 1000:
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


G_StatSHZ = SHZ_StatInfo()


# 玩游戏
class PlayActionSHZ(BaseAction):
    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '玩游戏'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务
        self.bet_cd = 1  # 下注间隔
        self.last_bet_tick = 0  # 上次开炮时间

    def do(self):
        state = self.client.client_state
        if state == ClientState.entered:
            self.on_begin()
        else:
            self.on_failed("当前未进入场景 ?")

    def update(self):
        if super(PlayActionSHZ, self).update():
            return True

        self.do_play()
        return False

    def do_bet(self):
        cmd = CMD_C_MainGameStart()
        cmd.bet_score = 1000
        cmd.line_count = 9
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MDM_GF_GAME, SUB_C_MainGameStart, s)

    # 模拟游戏逻辑
    def do_play(self):
        tm_now = time.time()
        if tm_now > self.last_bet_tick + self.bet_cd:
            self.last_bet_tick = tm_now
            if G_StatSHZ.is_need_run():
                self.do_bet()

    # 处理赌博结果
    def handle_bet_result(self, data):
        msg = CMD_S_MainGameResult()
        msg.ParseFromString(data)
        G_StatSHZ.add_score(msg.win_score)
        self.client.log("下注:%d,获得:%d" % (msg.bet_score, msg.win_score))

    @staticmethod
    def format_err(err_code):
        if err_code == 1:
            return "下注失败,没有足够的积分"
        elif err_code == 2:
            return "下注失败,没有小游戏次数"
        elif err_code == 3:
            return "下注失败,没有赢进不了比大小"
        elif err_code == 8:
            return "下注失败,下注筹码非法"
        return "下注失败,未知错误"

    def handle_bet_error(self, data):
        msg = CMD_S_ERROR()
        msg.ParseFromString(data)
        print(self.format_err(msg.err))

    # 处理网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id

        if msg_id == MDM_GF_GAME:
            if sub_msg_id == SUB_S_MainGameResult:
                self.handle_bet_result(msg.data)
            elif sub_msg_id == SUB_S_Error:
                self.handle_bet_error(msg.data)


# 水浒传用测试用例
class DemoCaseSHZ(BaseCase):
    def __init__(self):
        self.mac_start_idx = 138654493214311 + random.randint(0, 100000)  # my real mac 74-D4-35-B8-F8-B8
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        super(DemoCaseSHZ, self).__init__()

    # 创建测试客户端对象
    def build_guest(self):
        for i in range(self.robot_cnt):
            guest = GuestInfo()
            guest.machine_id = build_mac_addr(self.mac_start_idx + i)
            guest.client_version = 0
            guest.ip_address = "192.168.102.23"
            guest.client_kind = 501
            self.guests.append(guest)

    def build_ai(self, client):
        ai_list = super(DemoCaseSHZ, self).build_ai(client)
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
        ai_list.add_action(PlayActionSHZ(client))
        return ai_list
