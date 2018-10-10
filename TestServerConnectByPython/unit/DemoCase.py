# -*- coding: UTF-8 -*-
import random

from core.Action import *
from core.ActionGM import GMCMDAction
from protocal.CMD_Common_pb2 import *
from unit.BaseCase import BaseCase

if True:
    LOGIN_SERVER_IP = '192.168.101.109'
    LOGIN_SERVER_PORT = 8300
else:
    LOGIN_SERVER_IP = '192.168.0.218'
    LOGIN_SERVER_PORT = 8600

# 机器人数
ROBOT_COUNT = 10

# 玩游戏
class EnterHall(BaseAction):
    def __init__(self, client, timeout=2):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '进入大厅'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = True  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        cmd = CMD_C_ENTER_HALL()
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MDM_MB_LOGON, SUB_MB_ENTER_HALL, s)
        self.state = ActionState.doing

    def on_timeout(self):
        self.state = ActionState.timeout
        self.client.log("执行OK:" + self.action_name)


class GetGift(BaseAction):
    def __init__(self, client, timeout=3):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '领取礼包'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = True  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        cmd = CMD_C_GET_ONLINE_GIFT_CHECK_GET()
        cmd.user_id = self.client.role_base_info.user_id
        cmd.nType = random.randint(0, 2)
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MDM_MB_LOGON, SUB_MB_ENTER_HALL, s)
        self.state = ActionState.doing

    def on_timeout(self):
        self.state = ActionState.timeout
        self.client.log("执行OK:" + self.action_name)


class QueryUndeal(BaseAction):
    def __init__(self, client, timeout=1):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '漏单查询'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = True  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        cmd = CMD_C_QueryPurchaseUndealedTrade()
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MDM_MB_PURCHASE, SUB_MB_C2G_PURCHASE_QUERY_UNDEALED_TRADE, s)
        self.state = ActionState.doing

    def on_timeout(self):
        self.state = ActionState.timeout
        self.client.log("执行OK:" + self.action_name)


class QueryProductInfo(BaseAction):
    def __init__(self, client, timeout=1):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '充值项查询'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = True  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        cmd = CMD_MB_C2L_PRODUCT_INFO()
        cmd.user_id = self.client.role_base_info.user_id
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MDM_MB_PURCHASE, SUB_MB_C2L_PRODUCT_INFO, s)
        self.state = ActionState.doing

    def on_timeout(self):
        self.state = ActionState.timeout
        self.client.log("执行OK:" + self.action_name)


class QueryFirstPayInfo(BaseAction):
    def __init__(self, client, timeout=1):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '首充查询'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = True  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        self.client.client_session.send_data(MDM_MB_PURCHASE, SUB_MB_C2L_FIRST_PAY_INFO, '')
        self.state = ActionState.doing

    def on_timeout(self):
        self.state = ActionState.timeout
        self.client.log("执行OK:" + self.action_name)



# 演示用测试用例
class DemoCase(BaseCase):
    def __init__(self):
        self.mac_start_idx = 128454799203612 + random.randint(0, 10000) # my real mac 74-D4-35-B8-F8-B8
        self.robot_cnt = ROBOT_COUNT         # 定义测试用例测试的假人数量
        super(DemoCase, self).__init__()

    # 创建测试客户端对象
    def build_guest(self):
        for i in range(self.robot_cnt):
            guest = GuestInfo()
            guest.machine_id = build_mac_addr(self.mac_start_idx + i)

            print("guest.machine_id",guest.machine_id)
            guest.client_version = 0
            guest.ip_address = "192.168.101.109"
            self.guests.append(guest)

    def build_ai(self, client):
        ai_list = super(DemoCase, self).build_ai(client)

        # 随机延迟
        # ai_list.add_action(DelayAction(client, random.randint(0, 10)))
        connect_action = ConnectLsAction(client)
        connect_action.server_ip = LOGIN_SERVER_IP
        connect_action.server_port = LOGIN_SERVER_PORT
        ai_list.add_action(connect_action)
        ai_list.add_action(LoginAction(client))

        ai_list.add_action(ConnectGsAction(client))
        ai_list.add_action(LoginGSAction(client))
        ai_list.add_action(EnterScenceAction(client))
        ai_list.add_action(GMCMDAction(client, "@设置金币 %d" % 10000000))
        ai_list.add_action(PlayAction(client))
        return ai_list
