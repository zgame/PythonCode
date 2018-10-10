# -*- coding: UTF-8 -*-
from core.ActionGM import *
from protocal.CMD_BSMC_Game_pb2 import *
from protocal.CMD_SGJ_Game_pb2 import CMD_UserChip_C, CMD_StartGame_Single, CMD_GameResultinfo_S
from protocal.CMD_SHZ_Game_pb2 import CMD_S_MainGameResult, CMD_C_MainGameStart
from protocal.protocol_bsmc import *
from protocal.protocol_gs import *
from protocal.protocol_sgj import SUB_C_UserChip, SUB_C_StartGame_Single, SUB_S_GameResultInfo, SUB_S_SysMessage
from protocal.protocol_shz import SUB_S_MainGameResult, SUB_S_Error, SUB_C_MainGameStart
from unit.BaseCase import BaseCase

LOGIN_SERVER_IP = '192.168.101.85'
LOGIN_SERVER_PORT = 8300

# 机器人数
ROBOT_COUNT = 1
# 下注间隔
BET_CD = 3
# 下注额度
BET_SCORE = 1000
# 最大运行次数
MAX_RUNTIME = 20

# 测试起始金币
INIT_SCORE = 5000000
# 测试起始杀分游戏赞助值
INIT_KILL_AID = 1000
# 测试起始杀分大奖额度
INIT_KILL_USEABLE = 10000000
# 设置起始大奖池数量
INIT_PRIZE_POOL = 50000000000

# 水果机下注信息
# 第一个字段: 下注索引, 第二个字段: 下注分数, 第三个字段: 机器人作弊标记
BET_CHIP_ARR = [[3, 1000, 0], [1, 1000, 0]]

# 本测试用例主要用于测试给定金币贵族值等情况下一定开奖次数的金币曲线变化

class BetNode:
    def __init__(self):
        self.win_score = 0  # 每次赢得的分数
        self.left_score = 0  # 剩余分数


# 玩游戏
class PlayActionSGJ2(BaseAction):
    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '玩游戏'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务
        self.bet_cd = BET_CD  # 下注间隔
        self.last_bet_tick = 0  # 上次开炮时间
        self.result_list = []  # 记录每次开奖的状态
        self.run_time = 0  # 执行次数
        self.is_failed = False  # 执行失败,金币不足或其他原因
        self.left_score = INIT_SCORE
        self.bet_score = 0
        self.is_first = True

    def do(self):
        state = self.client.client_state
        if state == ClientState.entered:
            self.on_begin()
        else:
            self.on_failed("当前未进入场景 ?")

    def update(self):
        if super(PlayActionSGJ2, self).update():
            return True

        self.do_play()
        return False

    def do_bet(self):
        # 下注
        self.bet_score = 0
        if self.is_first:
            # self.is_first = False
            for k in BET_CHIP_ARR:
                chip = CMD_UserChip_C()
                chip.chip_index = k[0]
                chip.chip_value = k[1]
                self.bet_score += k[1]
                chip.android_cheat = k[2]
                s = chip.SerializeToString()
                self.client.client_session.send_data(MDM_GF_GAME, SUB_C_UserChip, s)
            # 开始
            cmd = CMD_StartGame_Single()
            cmd.user_cheat = False
            s2 = cmd.SerializeToString()
            self.client.client_session.send_data(MDM_GF_GAME, SUB_C_StartGame_Single, s2)
        else:
            cmd = CMD_StartGame_Single()
            cmd.user_cheat = True
            s2 = cmd.SerializeToString()
            self.client.client_session.send_data(MDM_GF_GAME, SUB_C_StartGame_Single, s2)

    # 模拟游戏逻辑
    def do_play(self):
        tm_now = time.time()
        if tm_now > self.last_bet_tick + self.bet_cd:
            self.last_bet_tick = tm_now
            if self.need_run():
                self.do_bet()

    def need_run(self):
        return self.run_time < MAX_RUNTIME and not self.is_failed

    def record_award(self, win_score):
        if self.run_time >= MAX_RUNTIME:
            return

        self.run_time += 1
        node = BetNode()
        node.win_score = win_score
        self.left_score = self.left_score - self.bet_score + win_score
        node.left_score = self.left_score
        self.result_list.append(node)
        if self.run_time >= MAX_RUNTIME:
            g_case_sgj2.on_action_ok(self)

    # 处理赌博结果
    def handle_bet_result(self, data):
        msg = CMD_GameResultinfo_S()
        msg.ParseFromString(data)
        self.record_award(msg.win_score_change)
        self.client.log("下注:%d,获得:%d" % (msg.chip_value, msg.win_score_change))

    # 处理网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id

        if msg_id == MDM_GF_GAME:
            if sub_msg_id == SUB_S_GameResultInfo:
                self.handle_bet_result(msg.data)
            elif sub_msg_id == SUB_S_SysMessage:
                self.handle_bet_error(msg.data)


# 宝石迷城演示用测试用例
class DemoCaseSGJ2(BaseCase):
    def __init__(self):
        self.mac_start_idx = 178654493214311 + random.randint(0, 1000000)  # my real mac 74-D4-35-B8-F8-B8
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        self.actions_ok = []
        self.action_ok_count = 0
        self.action_failed_count = 0
        self.bComplete = False
        super(DemoCaseSGJ2, self).__init__()

    def on_action_ok(self, action):
        self.action_ok_count += 1
        self.actions_ok.append(action)

    def on_action_failed(self):
        self.action_failed_count += 1

    def check_complete(self):
        if self.action_ok_count + self.action_failed_count >= ROBOT_COUNT:
            self.bComplete = True
            self.output_result()

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
        ai_list = super(DemoCaseSGJ2, self).build_ai(client)
        # 配置登录服务器
        connect_action = ConnectLsAction(client)
        connect_action.server_ip = LOGIN_SERVER_IP
        connect_action.server_port = LOGIN_SERVER_PORT
        ai_list.add_action(connect_action)
        # 登录
        ai_list.add_action(LoginAction(client))
        ai_list.add_action(ConnectGsAction(client))
        ai_list.add_action(LoginGSAction(client))
        ai_list.add_action(GMCMDOnceAction(client, "@设置游戏大奖池 %d" % INIT_PRIZE_POOL))
        ai_list.add_action(GMCMDAction(client, "@设置金币 %d" % INIT_SCORE))
        ai_list.add_action(GMCMDAction(client, "@设置杀分游戏赞助值 %d %d" % (INIT_KILL_AID, INIT_KILL_USEABLE)))
        ai_list.add_action(EnterScenceAction(client))
        ai_list.add_action(PlayActionSGJ2(client))
        return ai_list

    def update(self):
        if not self.bComplete:
            self.check_complete()

    def output_result(self):
        print ("--------------------bsmc2 result begin win----------------------")
        for action in self.actions_ok:
            lst_win = []
            for node in action.result_list:
                lst_win.append(str(node.win_score))
            print (" ".join(lst_win))
        print ("--------------------bsmc2 result begin left----------------------")
        for action in self.actions_ok:
            lst_left = []
            for node in action.result_list:
                lst_left.append(str(node.left_score))
            print (" ".join(lst_left))
        print ("--------------------bsmc2 result end----------------------")


g_case_sgj2 = DemoCaseSGJ2()
