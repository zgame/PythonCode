# -*- coding: UTF-8 -*-

from core.Action.Action import *
from core.Action.ConnectAction import ConnectAction
from core.Action.LoginAction import LoginAction
from core.Client import *
import protocal.cmd_common as Cmd
from protocal.cmd_brnn_pb2 import *

from unit.BaseCase import BaseCase

SERVER_IP = '127.0.0.1'
SERVER_PORT = 7301

# 机器人数
ROBOT_COUNT = 400
#机器人起始ID
ROBOT_Number=1001

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
        self.send_card_data = [] #  开牌信息
        self.area_my_scores = [] #  我的下注信息

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
        msg.chip_idx = random.randint(1, 4)
        msg.chip_coin = 10
        s = msg.SerializeToString()
        self.client.client_session.send_data(Cmd.GAME, Cmd.GAME_SUB_C_CHIP, s)
        print('on chip')

    def do_play(self):
        tmNow = time.time()
        if tmNow > self.last_chip + CHIP_CD:
            self.do_chip()

    # def handle_sitdown(self, data):
    #     msg = cmd_game_sitdown()
    #     msg.ParseFromString(data)
    #     self.client.log("坐下: table:%d, chair:%d, 在线人数:%d" % (msg.table_id, msg.chair_id, msg.param1))
    #
    # def get_state_str(self):
    #     if self.table_state == IDEL:
    #         return "等待"
    #     if self.table_state == CHIP:
    #         return "下注"
    #     if self.table_state == DRAW:
    #         return "开奖"
    #     if self.table_state == TRAD:
    #         return "结算"
    #
    # def get_area_str(self,areaindex):
    #     if areaindex == 0:
    #         return "庄家--"
    #     if areaindex == 1:
    #         return "天--"
    #     if areaindex == 2:
    #         return "地--"
    #     if areaindex == 3:
    #         return "玄--"
    #     if areaindex == 4:
    #         return "黄--"
    #
    # def get_card_type_str(self,cardtype):
    #     if cardtype == 0:
    #         return "无牛--"
    #     if cardtype == 1:
    #         return "牛1--"
    #     if cardtype == 2:
    #         return "牛2--"
    #     if cardtype == 3:
    #         return "牛3--"
    #     if cardtype == 4:
    #         return "牛4--"
    #     if cardtype == 5:
    #         return "牛5--"
    #     if cardtype == 6:
    #         return "牛6--"
    #     if cardtype == 7:
    #         return "牛7--"
    #     if cardtype == 8:
    #         return "牛8"
    #     if cardtype == 9:
    #         return "牛9--"
    #     if cardtype == 10:
    #         return "牛牛--"
    #     if cardtype == 11:
    #         return "四花牛--"
    #     if cardtype == 12:
    #         return "五花牛--"
    #     if cardtype == 13:
    #         return "炸弹--"
    #     if cardtype == 12:
    #         return "五小牛--"
    #
    # def get_win_or_lose_str(self,_type):
    #     if _type:
    #         return "(赢)"
    #     else:
    #         return "(输)"
    #
    # # 状态变更
    # def handle_table_state(self, data):
    #     msg = cmd_table_state()
    #     msg.ParseFromString(data)
    #     self.table_state = msg.state
    #     self.client.log("桌子状态变更:%s" % self.get_state_str())
    #     #  if msg.param1 is None:
    #     #      self.client.log("桌子状态变更:%s" % self.get_state_str())
    #     #  else:
    #     #      self.client.log("桌子状态变更:%s,%d" % (self.get_state_str(), msg.param1))
    #
    # def handle_table_draw(self, data):
    #     msg = cmd_table_draw()
    #     msg.ParseFromString(data)
    #     self.table_state = DRAW
    #     self.send_card_data = msg.send_card_data  # 开牌信息
    #     self.area_my_scores = msg.score  # 我的下注信息
    #     self.client.log("开始发牌-->所有人投注:%d,我的总投注:%d," % (msg.area_all_chips, msg.area_my_chips))
    #
    #     #  下注区域信息
    #     area_index = 0  # 区域索引
    #     for item in msg.send_card_data:
    #         sline = ""
    #         sline += "区域: %s" % self.get_area_str(area_index)
    #         sline += "牌类型: %s" % self.get_card_type_str(item.card_type)
    #
    #         cardStr = ""  #  牌
    #         for card in item.card_data:
    #             cardStr += ("%d" % card)+","
    #
    #         sline += "该区域的牌: %s" % cardStr
    #         if area_index > 0 :
    #             sline += "区域赔率: %d" % item.mutil
    #             sline += "区域总投注: %f" % item.area_total_result
    #             sline += "区域我的投注: %f" % self.area_my_scores[area_index]
    #             sline += "我的输赢情况: %s" % self.get_win_or_lose_str(item.player_win)
    #
    #         area_index = area_index + 1
    #         self.client.log(sline)
    #
    # def handle_online_count(self, data):
    #     msg = cmd_sync_player_onlinet_count()
    #     msg.ParseFromString(data)
    #     #  sline = "当前在线人数:%d" % msg.user_online_count
    #     #  self.client.log(sline)
    #
    # def handle_user_chip(self, data):
    #     msg = cmd_user_chip_resp()
    #     msg.ParseFromString(data)
    #     if msg.err_code == 0:
    #         self.client.log("下注成功:下注项:%s 金额: %f" % (self.get_area_str(msg.chip_idx), msg.chip_coin))
    #     else:
    #         self.client.log("下注失败,err:%d" % msg.err_code)
    #
    # def handle_chip_info(self, data):
    #     msg = cmd_chip_info()
    #     msg.ParseFromString(data)
    #     sline = "下注项:"
    #     for item in msg.chip_items:
    #         sline += "[%d,%f]" % (item.chip_idx, item.chip_coin)
    #     self.client.log(sline)
    #
    # def handle_user_trad(self, data):
    #     msg = cmd_user_trad()
    #     msg.ParseFromString(data)
    #     sline = "开奖ID: %d" % msg.user_id
    #     sline += "总投入: %f" % msg.area_my_chips
    #     sline += "总盈亏: %f" % msg.result_score
    #     sline += "当前剩余元宝: %f" % msg.now_coin
    #
    #     self.client.log(sline)
    #
    # # 处理网络消息处理
    # def handle_net_msg(self, msg):
    #     msg_id = msg.msg_id
    #     sub_msg_id = msg.sub_msg_id
    #
    #     if msg_id == Cmd.GAME:
    #         if sub_msg_id == Cmd.GAME_SUB_S_SITDOWN:
    #             self.handle_sitdown(msg.data)
    #         elif sub_msg_id == Cmd.GAME_SUB_S_STATE_CHG:
    #             self.handle_table_state(msg.data)
    #         elif sub_msg_id == Cmd.GAME_SUB_S_DRAW:
    #             self.handle_table_draw(msg.data)
    #         elif sub_msg_id == Cmd.GAME_SUB_S_CHIP:
    #             self.handle_user_chip(msg.data)
    #         elif sub_msg_id == Cmd.GAME_SUB_S_CHIP_INFO:
    #             self.handle_chip_info(msg.data)
    #         elif sub_msg_id == Cmd.GAME_SUB_S_USER_TRAD:
    #             self.handle_user_trad(msg.data)
    #         elif sub_msg_id == Cmd.GAME_SUB_S_ONLINET_COUNT:
    #             self.handle_online_count(msg.data)
    #     if msg_id == Cmd.COMMON:
    #         if sub_msg_id == Cmd.COMMON_SUB_S_ROLL_MSG:
    #             self.handle_roll_msg(msg.data)


# 水浒传用测试用例
class DemoCaseBrnn(BaseCase):
    def __init__(self):
        self.start_user_id = ROBOT_Number #定义测试机器人开始的ID
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        super(DemoCaseBrnn, self).__init__()

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
        ai_list = super(DemoCaseBrnn, self).build_ai(client)

        # 配置登录服务器
        connect_action = ConnectAction(client)
        connect_action.server_ip = SERVER_IP
        connect_action.server_port = SERVER_PORT
        ai_list.add_action(connect_action)

        # 登录
        ai_list.add_action(LoginAction(client))
        ai_list.add_action(PlayActionFqzs(client))

        return ai_list

brnn_fqzs = DemoCaseBrnn()
