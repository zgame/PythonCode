# -*- coding: UTF-8 -*-
from Client import *
from core.Action import *
from protocal.CMD_Common_pb2 import *


# GM指令等

# GM指令
class GMCMDAction(BaseAction):
    def __init__(self, client, text, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = 'GM指令:' + text  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = True  # 任务失败是否执行下一个任务,用于某些非重要任务
        self.bResponse = False
        self.text = text

    def do(self):
        self.state = ActionState.doing
        msg = CMD_GM_CMD()
        msg.cmd = self.text
        s = msg.SerializeToString()
        self.client.client_session.send_data(MDM_GF_GMCMD, GMCMD_CMD, s)

    def update(self):
        if super(GMCMDAction, self).update():
            return True
        if self.bResponse:
            self.on_success()

    def handle_cmd_rsp(self, data):
        msg = CMD_GM_CMD_RESP()
        msg.ParseFromString(data)
        self.bResponse = True
        self.client.log(msg.text)

    # 处理网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id

        if msg_id == MDM_GF_GMCMD:
            if sub_msg_id == GMCMD_CMD_RESP:
                self.handle_cmd_rsp(msg.data)


# 只执行一次的gm指令,用于设置系统数据等
class GMCMDOnceAction(GMCMDAction):
    mDictRun = {}  # 已运行的指令集合,静态变量
    mLock = threading.RLock()  # 锁,静态变量

    def __init__(self, client, text, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = 'GM指令(执行一次):' + text  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = True  # 任务失败是否执行下一个任务,用于某些非重要任务
        self.bResponse = False
        self.text = text

    def need_do(self):
        AutoLock(self.mLock)
        if self.text in self.mDictRun.keys():
            return False
        self.mDictRun[self.text] = 1
        return True

    def do(self):
        if not self.need_do():
            self.on_ignore()
            return True

        self.state = ActionState.doing
        msg = CMD_GM_CMD()
        msg.cmd = self.text
        s = msg.SerializeToString()
        self.client.client_session.send_data(MDM_GF_GMCMD, GMCMD_CMD, s)
