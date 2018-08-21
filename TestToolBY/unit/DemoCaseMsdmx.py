# -*- coding: UTF-8 -*-

from core.Action.Action import *
from core.Action.ConnectAction import ConnectAction
from core.Action.LoginAction import LoginAction
from core.Client import *
import protocal.cmd_common as Cmd
from protocal.cmd_msdmx_pb2 import *

from unit.BaseCase import BaseCase

SERVER_IP = '127.0.0.1'
SERVER_PORT = 7701

# 机器人数
ROBOT_COUNT = 200
#机器人起始ID
ROBOT_Number=801

CHIP_CD = 3

CHIP_LIST = [10, 20, 50, 100, 200, 500, 1000]


# 玩游戏
class PlayActionMsdmx(BaseAction):
    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '玩游戏'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务
        self.bet_cd = CHIP_CD  # 下注间隔
        self.last_bet_tick = 0  # 上次开炮时间
        self.level = 1  # 关卡
        self.brick = 0  # 当前关卡消除的砖块数量
        self.bEnter = False

    def do(self):
        state = self.client.client_state
        if state == ClientState.entered or state == ClientState.logined:
            self.on_begin()
        else:
            self.on_failed("当前未进入场景 ?")

    def update(self):
        if super(PlayActionMsdmx, self).update():
            return True

        self.do_play()
        return False

    # 普通下注
    def do_bet(self):
        cmd = cmd_sub_c_bet()
        cmd.bet_score = random.choice(CHIP_LIST)
        s = cmd.SerializeToString()
        self.client.client_session.send_data(Cmd.GAME, Cmd.GAME_SUB_C_CHIP, s)


    # 通关抽奖
    def do_award(self):
        cmd = cmd_sub_c_award()
        s = cmd.SerializeToString()
        self.client.client_session.send_data(Cmd.GAME, Cmd.GAME_SUB_C_CHIP_EX, s)

    # 模拟游戏逻辑
    def do_play(self):
        tm_now = time.time()
        if tm_now > self.last_bet_tick + self.bet_cd:
            self.last_bet_tick = tm_now
            self.do_bet()

    # # 接收游戏配置
    # def handle_game_config(self, data):
    #     self.client.log("收到美食大冒险游戏配置!")
    #
    # # 处理游戏数据
    # def handle_game_data(self, data):
    #     msg = cmd_gameinfo_s()
    #     msg.ParseFromString(data)
    #     self.level = msg.level
    #     self.brick = msg.brick
    #     self.bEnter = True
    #     self.client.log("接收游戏数据:关卡-%d,砖块-%d" % (self.level, self.brick))
    #
    # # 处理赌博结果
    # def handle_bet_result(self, data):
    #     msg = cmd_sub_s_bet()
    #     msg.ParseFromString(data)
    #     if msg.error_code == 0:
    #         self.client.log(
    #             "%d x %d 下注:%d,获得:%d" % (msg.data.size, msg.data.size, msg.data.bet_score, msg.data.get_score))
    #     elif msg.error_code == 4:
    #         self.do_award()
    #     else:
    #         self.client.log("投注失败,错误码:%d" % msg.error_code)
    #
    # # 处理网络消息处理
    # def handle_net_msg(self, msg):
    #     msg_id = msg.msg_id
    #     sub_msg_id = msg.sub_msg_id
    #
    #     if msg_id == Cmd.GAME:
    #         if sub_msg_id == Cmd.GAME_SUB_S_GAMECONFIG:
    #             self.handle_game_config(msg.data)
    #         elif sub_msg_id == Cmd.GAME_SUB_S_SITDOWN:
    #             self.handle_game_data(msg.data)
    #         elif sub_msg_id == Cmd.GAME_SUB_S_CHIP:
    #             self.handle_bet_result(msg.data)
    #         elif sub_msg_id == Cmd.GAME_SUB_S_CHIP_EX:
    #             self.handle_award_result(msg.data)
    #     if msg_id == Cmd.COMMON:
    #         if sub_msg_id == Cmd.COMMON_SUB_S_ROLL_MSG:
    #             self.handle_roll_msg(msg.data)


# 水浒传用测试用例
class DemoCaseMsdmx(BaseCase):
    def __init__(self):
        self.start_user_id = ROBOT_Number #定义测试机器人开始的ID
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        super(DemoCaseMsdmx, self).__init__()

    # 创建测试客户端对象
    def build_guest(self):
        for i in range(self.robot_cnt):
            guest = GuestInfo()
            guest.user_id = self.start_user_id + i
            guest.machine_id = '08-00-27-00-CC-77'
            guest.client_version = 1
            guest.ip_address = "127.0.0.1"
            guest.client_kind = 1
            guest.game_kind = 100
            self.guests.append(guest)

    def build_ai(self, client):
        ai_list = super(DemoCaseMsdmx, self).build_ai(client)

        # 配置登录服务器
        connect_action = ConnectAction(client)
        connect_action.server_ip = SERVER_IP
        connect_action.server_port = SERVER_PORT
        ai_list.add_action(connect_action)

        # 登录
        ai_list.add_action(LoginAction(client))
        ai_list.add_action(PlayActionMsdmx(client))
        return ai_list


unit_msdmx = DemoCaseMsdmx()
