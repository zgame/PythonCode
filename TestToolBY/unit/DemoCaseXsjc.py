# -*- coding: UTF-8 -*-

from core.Action.Action import *
from core.Action.ConnectAction import ConnectAction
from core.Action.LoginAction import LoginAction
from core.Client import *
import protocal.cmd_common as Cmd
from protocal.cmd_xsjc_pb2 import *
from unit.BaseCase import BaseCase

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8301

# 机器人数
ROBOT_COUNT = 100
#机器人起始ID
ROBOT_Number=1

CHIP_CD = 2

typeList=[1,2,3] #竞猜大类  总表gametype 1 2 3
compid__ball_1=33
compid_world_2=3001
compid_real_3=64
subID=1 #竞猜子项ID  kindtype  1-12 2-1234 3-1
optionID=1 #押注项ID resultid
option2=0 #四强后面需要填写
option3=0
option4=0
coin=100    #下注金额
chipCountList=[1,2,3] #下注数量


class PlayActionXsjc(BaseAction):
    def __init__(self,client,timeout=0):
      self.client = client
      self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
      self.action_name = '玩游戏'  # 任务名称
      self.state = ActionState.none  # 状态
      self.time_begin = 0  # 任务开始时间
      self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务
      self.table_state = 0  # 桌子状态
      self.last_chip = 0  # 上一次下注时间

    def do(self):
        print('Do Action')
        state = self.client.client_state
        if state == ClientState.logined:
            self.on_begin()
        else:
            self.on_failed("当前未进入场景 ?")

    def update(self):
        if super(PlayActionXsjc,self).update():
             return True


        self.do_play()
        return False

    def do_chip(self):
         self.last_chip=time.time()
         msg=CMD_C_Chip()
         msg.type=random.choice(typeList)
         msg.subID=subID
         if msg.type == 1:
            msg.compID=compid__ball_1
         elif msg.type==2:
            msg.compID=compid_world_2
         elif msg.type==3:
            msg.compID=compid_real_3
         msg.optionID=optionID
         msg.option2=option2
         msg.option3=option2
         msg.option4=option4
         msg.coin=coin
         msg.chipCount=random.choice(chipCountList)
         s = msg.SerializeToString()
         self.client.log("下注参数: type:%d, subid:%d,comid %d,optionid %d" % (msg.type, msg.subID,msg.compID,msg.optionID))
         self.client.client_session.send_data(Cmd.GAME, Cmd.GAME_SUB_C_CHIP, s)


    def do_play(self):
        tmNow = time.time()
        if tmNow>self.last_chip+CHIP_CD:

            self.do_chip()

    def handle_enter(self, data):
         self.client.log("%d 进入游戏场景" % self.client.guest_info.user_id)


    # 处理网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id

        if msg_id == Cmd.GAME:
            if sub_msg_id == Cmd.GAME_SUB_S_SITDOWN:
                self.handle_enter(msg.data)





# 水浒传用测试用例
class DemoCaseXsjc(BaseCase):
    def __init__(self):
        self.start_user_id = ROBOT_Number #定义测试机器人开始的ID
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        super(DemoCaseXsjc, self).__init__()

    # 创建测试客户端对象
    def build_guest(self):
        print('Do Login')
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
        ai_list = super(DemoCaseXsjc, self).build_ai(client)

        # 配置登录服务器
        connect_action = ConnectAction(client)
        connect_action.server_ip = SERVER_IP
        connect_action.server_port = SERVER_PORT
        ai_list.add_action(connect_action)

        # 登录
        ai_list.add_action(LoginAction(client))
        ai_list.add_action(PlayActionXsjc(client))
        return ai_list

unit_xsjc=DemoCaseXsjc()