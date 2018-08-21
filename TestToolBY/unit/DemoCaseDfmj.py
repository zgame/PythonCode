# -*- coding: UTF-8 -*-

from core.Action.Action import *
from core.Action.ConnectAction import ConnectAction
from core.Action.LoginAction import LoginAction
from core.Client import *
import protocal.cmd_common as Cmd
from protocal.cmd_dfmj_pb2 import *

from unit.BaseCase import BaseCase

SERVER_IP = '127.0.0.1'
SERVER_PORT = 7601

# 机器人数
ROBOT_COUNT = 10
#机器人起始ID
ROBOT_Number=1
CHIP_CD = 3

LINE_CONT = 9
CHIP_LIST = [100, 200, 500, 1000, 2000, 5000, 10000]


# 玩游戏
class PlayActionDfmj(BaseAction):
    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '玩游戏'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务
        self.table_state = 0  # 桌子状态
        self.last_chip = 0  # 上一次下注时间
        self.need_do_mary = False  # 是否开小玛丽

    def do(self):
        state = self.client.client_state
        if state == ClientState.logined:
            self.on_begin()
        else:
            self.on_failed("当前未进入场景 ?")

    def update(self):
        if super(PlayActionDfmj, self).update():
            return True

        self.do_play()
        return False

    # 正常投注
    def do_play(self):
        tmNow = time.time()
        if tmNow > self.last_chip + CHIP_CD:
            if self.need_do_mary:
                self.need_do_mary = False
                self.do_play_mary()
            else:
                self.do_chip()

    # 下注
    def do_chip(self):
        self.last_chip = time.time()
        global CHIP_LIST
        msg = cmd_c_maingamestart()
        msg.bet_score = random.choice(CHIP_LIST)
        msg.line_count = LINE_CONT
        s = msg.SerializeToString()
        self.client.client_session.send_data(Cmd.GAME, Cmd.GAME_SUB_C_CHIP, s)

    # # 小玛丽
    # def do_play_mary(self):
    #     msg = cmd_c_marygamestart()
    #     s = msg.SerializeToString()
    #     self.client.client_session.send_data(Cmd.GAME, Cmd.GAME_SUB_C_CHIP_EX, s)
    #
    # def handle_enter(self, data):
    #     self.client.log("%d 进入游戏场景" % self.client.guest_info.user_id)
    #
    # # 开奖结果
    # def handle_game_result(self, data):
    #     msg = cmd_s_maingameresult()
    #     msg.ParseFromString(data)
    #     if msg.error_code == 0:
    #         self.client.log("下注成功:%d, 下注额:%d x 9, 得分:%d" % (self.client.guest_info.user_id,
    #                                                         msg.bet_score, msg.win_score))
    #         if msg.bonus_game_count > 0:
    #             self.need_do_mary = True
    #     else:
    #         self.client.log("下注失败,下注额:%d, err:%d" % (msg.bet_score, msg.error_code))
    #
    # # 处理小玛丽开奖结果
    # def handle_mary_result(self, data):
    #     msg = cmd_s_marygameresult()
    #     msg.ParseFromString(data)
    #     if msg.error_code == 0:
    #         self.client.log("小玛丽开奖:")
    #         for result in msg.mary_result:
    #             self.client.log("\t当前次数:%d,本地得分:%d" % (result.curr_game_count, result.win_score))
    #     else:
    #         self.client.log("小玛丽开奖失败,err:" % msg.error_code)
    #
    # 处理网络消息处理
    # def handle_net_msg(self, msg):
    #     msg_id = msg.msg_id
    #     sub_msg_id = msg.sub_msg_id
    #
    #     if msg_id == Cmd.GAME:
    #         if sub_msg_id == Cmd.GAME_SUB_S_SITDOWN:
    #            #self.handle_enter(msg.data)
    #            print '1'
    #         elif sub_msg_id == Cmd.GAME_SUB_S_CHIP:
    #             #self.handle_game_result(msg.data)
    #             print '1'
    #         elif sub_msg_id == Cmd.GAME_SUB_S_CHIP_EX:
    #             #self.handle_mary_result(msg.data)
    #             print '1'
    #     if msg_id == Cmd.COMMON:
    #         if sub_msg_id == Cmd.COMMON_SUB_S_ROLL_MSG:
    #             #self.handle_roll_msg(msg.data)
    #             print '1'


# 水浒传用测试用例
class DemoCaseDfmj(BaseCase):


    def __init__(self):
        self.start_user_id = ROBOT_Number
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        super(DemoCaseDfmj, self).__init__()

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
        ai_list = super(DemoCaseDfmj, self).build_ai(client)

        # 配置登录服务器
        connect_action = ConnectAction(client)
        connect_action.server_ip = SERVER_IP
        connect_action.server_port = SERVER_PORT
        ai_list.add_action(connect_action)

        # 登录
        ai_list.add_action(LoginAction(client))
        ai_list.add_action(PlayActionDfmj(client))
        return ai_list


unit_dfmj = DemoCaseDfmj()
