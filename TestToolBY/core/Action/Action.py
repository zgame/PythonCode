# -*- coding: UTF-8 -*-
from core.Client import *


# 登录进游戏等公共行为

class ActionState(object):
    none = 0            # 未开始
    doing = 1           # 正在执行
    timeout = 2         # 超时
    success = 3         # 执行成功
    failed = 4          # 执行失败
    ignore = 5          # 忽略


# 基础行为
class BaseAction(object):

    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '未知'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = True  # 任务失败是否执行下一个任务,用于某些非重要任务

    def on_begin(self):
        self.time_begin = time.time()
        self.state = ActionState.doing
        self.client.log("开始执行:"+self.action_name)

    def on_failed(self, reason=''):
        self.state = ActionState.failed
        if len(reason) > 0:
            self.client.log("执行失败:%s, 原因:%s" % (self.action_name, reason))
        else:
            self.client.log("执行失败:%s" + self.action_name)

    def on_success(self):
        self.state = ActionState.success
        self.client.log("执行成功:" + self.action_name)
        self.result_assert()

    def on_timeout(self):
        self.state = ActionState.timeout
        self.client.log("执行超时:" + self.action_name)

    def on_ignore(self):
        self.state = ActionState.ignore

    def is_complete(self):
        return self.state == ActionState.timeout\
               or self.state == ActionState.success\
               or self.state == ActionState.failed\
               or self.state == ActionState.ignore

    def is_valid(self):
        return self.client is not None

    def do(self):
        pass

    def handle_net_msg(self, msg):
        pass

    def result_assert(self):
        pass

    def update(self):
        if self.time_out > 0:
            if time.time() - self.time_begin >= self.time_out:
                self.on_timeout()
                return True
        return False


class ActionList(BaseAction):

    def __init__(self):
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = True  # 任务失败是否执行下一个任务,用于某些非重要任务
        self.action_list = []
        self.action_idx = 0

    def is_valid(self):
        return len(self.action_list) > 0

    def add_action(self, action):
        if action is None or not isinstance(action, BaseAction) or not action.is_valid():
            return False

        if not action.failed_continue:
            self.failed_continue = False
        self.action_list.append(action)
        return True

    def current_action(self):
        if not self.is_valid():
            return None
        if self.action_idx >= len(self.action_list):
            return None
        action = self.action_list[self.action_idx]
        return action

    def handle_net_msg(self, msg):
        action = self.current_action()
        if action is not None and action.is_valid():
            action.handle_net_msg(msg)

    def do(self):
        self.action_idx = 0
        action = self.current_action()
        if action is not None and action.is_valid():
            self.state = ActionState.doing
            action.do()

    def update(self):
        if self.is_complete():
            return True

        if self.action_idx >= len(self.action_list):
            self.state = ActionState.success
            return True

        action = self.action_list[self.action_idx]
        if action is None:
            self.state = ActionState.success
            return True

        if action.is_complete():
            if action.state == ActionState.failed and not action.failed_continue:
                self.state = ActionState.failed
                return True
            else:
                self.action_idx += 1
                return True
        elif action.state == ActionState.none:
            action.do()
        else:
            action.update()

# 延迟ai
class DelayAction(BaseAction):

    def __init__(self, client, timeout=5):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '延迟'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = True  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        self.on_begin()

    def on_timeout(self):
        self.on_success()
