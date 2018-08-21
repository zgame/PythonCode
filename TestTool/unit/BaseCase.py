# -*- coding: UTF-8 -*-
from core.Action.Action import ActionList


class BaseCase(object):
    def __init__(self):
        self.guests = []
        self.build_guest()

    # 创建测试客户端对象
    def build_guest(self):
        pass

    # 创建测试流程
    def build_ai(self, client):
        ai = ActionList()
        return ai

    def update(self):
        pass
