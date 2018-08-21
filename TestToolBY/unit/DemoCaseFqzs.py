# -*- coding: UTF-8 -*-

from core.Action.Action import *
from core.Action.ConnectAction import ConnectAction
from core.Action.LoginAction import LoginAction
from core.Client import *
import protocal.cmd_common as Cmd
from protocal.cmd_chzb_pb2 import *

from unit.BaseCase import BaseCase

SERVER_IP = '127.0.0.1'
SERVER_PORT = 7201

# 机器人数
ROBOT_COUNT = 100

CHIP_CD = 2

EMPTY = 0
IDEL = 1  # 等待开始
CHIP = 2  # 下注状态
DRAW = 3  # 开奖
TRAD = 4  # 结算, 该游戏好像不需要


# 玩游戏
class PlayActionFqzs(BaseAction):
    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '玩游戏'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务
        self.table_state = 0  # 桌子状态
        self.last_chip = 0  # 上一次下注时间

    def do(self):
        state = self.client.client_state
        if state == ClientState.logined:
            self.on_begin()
        else:
            self.on_failed("当前未进入场景 ?")

    def update(self):
        if super(PlayActionFqzs, self).update():
            return True

        self.do_play()
        return False

    # 下注
    def do_chip(self):
        self.last_chip = time.time()
        msg = cmd_user_chip()
        msg.user_id = self.client.role_base_info.user_id
        msg.chip_idx = random.randint(1, 10)
        msg.chip_coin = 1
        s = msg.SerializeToString()
        self.client.client_session.send_data(Cmd.GAME, Cmd.GAME_SUB_C_CHIP, s)

    def do_play(self):
        tmNow = time.time()
        if self.table_state == CHIP and tmNow > self.last_chip + CHIP_CD:
            self.do_chip()

    def handle_sitdown(self, data):
        msg = cmd_game_sitdown()
        msg.ParseFromString(data)
        self.client.log("坐下: table:%d, chair:%d" % (msg.table_id, msg.chair_id))

    def get_state_str(self):
        if self.table_state == IDEL:
            return "等待"
        if self.table_state == CHIP:
            return "下注"
        if self.table_state == DRAW:
            return "开奖"
        if self.table_state == TRAD:
            return "结算"

    # 状态变更
    def handle_table_state(self, data):
        msg = cmd_table_state()
        msg.ParseFromString(data)
        self.table_state = msg.state
        if msg.param1 is None:
            self.client.log("桌子状态变更:%s" % self.get_state_str())
        else:
            self.client.log("桌子状态变更:%s,%d" % (self.get_state_str(), msg.param1))

    def handle_table_draw(self, data):
        msg = cmd_table_draw()
        msg.ParseFromString(data)
        self.table_state = DRAW
        self.client.log("开奖结果:%d" % msg.award_id)

    def handle_user_chip(self, data):
        msg = cmd_user_chip_resp()
        msg.ParseFromString(data)
        if msg.err_code == 0:
            self.client.log("下注成功:%d, %f" % (msg.chip_idx, msg.chip_coin))
        else:
            self.client.log("下注失败,err:%d" % msg.err_code)

    def handle_chip_info(self, data):
        msg = cmd_chip_info()
        msg.ParseFromString(data)
        sline = "下注项:"
        for item in msg.chip_items:
            sline += "[%d,%f]" % (item.chip_idx, item.chip_coin)
        self.client.log(sline)

    def handle_user_trad(self, data):
        msg = cmd_user_trad()
        msg.ParseFromString(data)
        sline = "开奖获得: %d" % msg.user_id
        for item in msg.chip_items:
            sline += "[%d,%f,%f]" % (item.chip_idx, item.chip_coin, item.chip_award)
        self.client.log(sline)

    def handle_roll_msg(self, data):
        msg = cmd_roll_message()
        msg.ParseFromString(data)
        self.client.log("跑马灯:" + msg.message)

    # 处理网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id

        if msg_id == Cmd.GAME:
            if sub_msg_id == Cmd.GAME_SUB_S_SITDOWN:
                self.handle_sitdown(msg.data)
            elif sub_msg_id == Cmd.GAME_SUB_S_STATE_CHG:
                self.handle_table_state(msg.data)
            elif sub_msg_id == Cmd.GAME_SUB_S_DRAW:
                self.handle_table_draw(msg.data)
            elif sub_msg_id == Cmd.GAME_SUB_S_CHIP:
                self.handle_user_chip(msg.data)
            elif sub_msg_id == Cmd.GAME_SUB_S_CHIP_INFO:
                self.handle_chip_info(msg.data)
            elif sub_msg_id == Cmd.GAME_SUB_S_USER_TRAD:
                self.handle_user_trad(msg.data)
        if msg_id == Cmd.COMMON:
            if sub_msg_id == Cmd.COMMON_SUB_S_ROLL_MSG:
                self.handle_roll_msg(msg.data)


# 水浒传用测试用例
class DemoCaseFqzs(BaseCase):
    def __init__(self):
        self.start_user_id = 801
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        super(DemoCaseFqzs, self).__init__()

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
        ai_list = super(DemoCaseFqzs, self).build_ai(client)

        # 配置登录服务器
        connect_action = ConnectAction(client)
        connect_action.server_ip = SERVER_IP
        connect_action.server_port = SERVER_PORT
        ai_list.add_action(connect_action)

        # 登录
        ai_list.add_action(LoginAction(client))
        ai_list.add_action(PlayActionFqzs(client))
        return ai_list


unit_chzb = DemoCaseFqzs()
