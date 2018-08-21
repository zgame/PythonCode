# -*- coding: UTF-8 -*-
from Action import *


# 登录
class LoginAction(BaseAction):

    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '登录'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        state = self.client.client_state
        if state == ClientState.connected:
            self.on_begin()
            self.client.login()
        else:
            self.on_failed("未连接登录服务器")



    def update(self):
        if super(LoginAction, self).update():
            return True
        state = self.client.client_state
        if state == ClientState.logined:
            self.on_success()
        elif state == ClientState.login_failed:
            self.on_failed("登录失败")
        return False
