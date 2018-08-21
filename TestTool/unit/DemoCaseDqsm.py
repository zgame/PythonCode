# -*- coding: UTF-8 -*-

from core.Action.Action import *
from core.Action.ConnectAction import ConnectAction
from core.Action.LoginAction import LoginAction
from core.Client import *
import protocal.cmd_common as Cmd
from protocal.cmd_dqsm_pb2 import *
from unit.BaseCase import BaseCase

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8301

# 机器人数
ROBOT_COUNT = 200
#机器人起始ID
ROBOT_Number=1

CHIP_CD = 2

class PlayActionDqsm(BaseAction):
    def __init__(self):
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
        if super(PlayActionDqsm,self).update():
             return True

        self.do_play()
        return False

    def do_chip(self):
        self.last_chip = time.time()
        msg=cmd_c_chip()
