# -*- coding: UTF-8 -*-

from core.Action.Action import *
from core.Action.ConnectAction import ConnectAction
from core.Action.LoginAction import LoginAction
from core.Client import *
import protocal.cmd_common as Cmd
from protocal.cmd_jcby_pb2 import *

from unit.BaseCase import BaseCase

SERVER_IP = '127.0.0.1'
SERVER_PORT = 7101

# 机器人数
ROBOT_COUNT = 10
#机器人起始ID
ROBOT_Number=1

CHIP_CD = 2     #发射子弹间隔

EMPTY = 0
HALL = 1  # 大厅中
ROOM = 2  # 鱼池中


# 选择房间
class SelectRoomAction(BaseAction):

    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '选择房间'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        state = self.client.client_state
        if state == ClientState.logined:
            self.on_begin()
            self.select_room()
            #self.client.entered()
        else:
            self.on_failed("未连接登录服务器")

    # 选择房间
    def select_room(self):
        msg = cmd_c_select_room()
        msg.user_id = self.client.role_base_info.user_id
        print("用户ID%d" % self.client.role_base_info.user_id)
        # msg.user_id = 1
        msg.cell_score = 10
        self.table_state = ROOM
        s = msg.SerializeToString()
        self.client.client_session.send_data(Cmd.GAME, Cmd.GAME_SUB_C_SELECT_ROOM, s)

    def update(self):
        if super(SelectRoomAction, self).update():
            return True
        state = self.client.client_state
        if state == ClientState.logined:
            self.on_success()
        elif state == ClientState.login_failed:
            self.on_failed("登录失败")
        return False


# 玩游戏
class PlayActionJcby(BaseAction):
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
        if super(PlayActionJcby, self).update():
            return True

        self.do_play()
        return False



    def do_fire(self):
        tmNow = time.time()
        if self.table_state == ROOM and tmNow > self.last_chip + CHIP_CD:
            self.last_chip = time.time()

            msg = cmd_c_user_fire()
            msg.user_id = self.client.role_base_info.user_id
            self.client.role_base_info.fire_cnt=self.client.role_base_info.fire_cnt+1
            msg.bullet_temp_id = self.client.role_base_info.fire_cnt
            msg.bullet_angle = random.randint( 0,180)
            msg.bullet_mulriple = 1
            s = msg.SerializeToString()
            self.client.client_session.send_data(Cmd.GAME, Cmd.GAME_SUB_C_USER_FIRE, s)
            print("do fire")


    def do_play(self):
        tmNow = time.time()
        if tmNow > self.last_chip + CHIP_CD:
            self.do_fire()

    # 处理网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id

        sub_msg_id = msg.sub_msg_id
        if self.table_state != ROOM:
            self.table_state = ROOM
            print("消息ID%d" % Cmd.GAME)
        if msg_id == Cmd.GAME:
            # if sub_msg_id == Cmd.GAME_SUB_S_ROOM_LIST:
            #     print('房间信息')
            #     self.handle_room_list( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_SELECT_ROOM:
            #     self.handle_select_room( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_ENTER_SCENE:
            #     self.handle_enter_scene( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_EXIT_SCENE:
            #     self.handle_exit_scene( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_OTHER_ENTER_SCENE:
            #     self.handle_other_enter_scene( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_SCENE_FISH:
            #     self.handle_scene_fish( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_DISTRIBUTE_FISH:
            #     self.handle_create_fish( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_USER_FIRE:
            #     self.handle_user_fire( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_CATCH_FISH:
            #     self.handle_catch_fish( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_CHANGE_BULLET:
            #     self.handle_change_bullet( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_SWITCH_SCENE:
            #     self.handle_switch_scene( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_BOSS_COME:
            #     self.handle_boss_come( msg.data)
            # elif sub_msg_id == Cmd.GAME_SUB_S_UPDATE_SCORE:
            #     self.handle_update_score( msg.data)




            if sub_msg_id == Cmd.GAME_SUB_S_SCENE_FISH:
                self.handle_scene_fish( msg.data)
            elif sub_msg_id == Cmd.GAME_SUB_S_USER_FIRE:
                self.handle_user_fire( msg.data)
            elif sub_msg_id == Cmd.GAME_SUB_S_CATCH_FISH:
                self.handle_catch_fish( msg.data)


        if msg_id == Cmd.COMMON:
            if sub_msg_id == Cmd.COMMON_SUB_S_ROLL_MSG:
                self.handle_roll_msg(msg.data)

    def handle_room_list(self, data):
        msg = cmd_s_room_list()
        msg.ParseFromString(data)
        self.client.log( "房间数量：" + len(msg.room_list))
        self.table_state = HALL;
        notif = cmd_c_select_room()
        notif.user_id = self.client.role_base_info.user_id
        notif.cell_score = 1;
        s = msg.SerializeToString()
        self.client.client_session.send_data(Cmd.GAME, Cmd.GAME_SUB_C_USER_FIRE, s)

    def handle_select_room(self, data):
        msg = cmd_s_select_room()
        msg.ParseFromString( data)
        if msg.result_code:
            self.client.log("玩家%d进入到 %d房间" % (msg.user_id, msg.cell_score))
        else:
            self.client.log("金币不足，不能进入房间")

    def handle_enter_scene(self, data):
        self.table_state = ROOM;
        msg = cmd_s_enter_scene()
        msg.ParseFromString( data)
        self.client.log("%d个玩家在%d房间里" % (len(msg.table_users), msg.scene_id))

    def handle_other_enter_scene(self,data):
        msg = cmd_s_other_enter_scene()
        msg.ParseFromString( msg.data)
        self.client.log("玩家%s进入房间" % (msg.user_info.nick_name))

    def handle_exit_scene(self, data):
        msg = cmd_s_exit_scene()
        msg.ParseFromString( data)
        self.client.log( "退出房间")

    def handle_scene_fish(self,data):
        msg = cmd_s_scene_fish()
        msg.ParseFromString( data)
        self.client.log("场景里有%d条鱼" % (len(data.scene_fishs)))

    def handle_create_fish(self,data):
        msg = cmd_s_distribute_fish()
        msg.ParseFromString( data)
        self.client.log("生成%d条鱼：ID%d" % (len(data.fishs), data.fishs[0].uid))

    def handle_user_fire(self,data):
        msg = cmd_s_user_fire()
        msg.ParseFromString( data)
        self.client.log("座位号" + msg.chair_id	 + "开炮")

    def handle_catch_fish(self,data):
        msg = cmd_s_catch_fish()
        msg.ParseFromString( data)
        self.client.log("用户%d捕获到鱼获得%d" % (data.user_id, data.curr_score))

    def handle_change_bullet(self, data):
        msg = cmd_s_change_bullet()
        msg.ParseFromString( data)
        self.client.log("玩家%d更换了%f倍炮" % (data.user_id, data.bullet_mulriple))

    def handle_switch_scene(self,data):
        msg = cmd_s_switch_scene()
        msg.ParseFromString( data)
        self.client.log("切换场景")

    def handle_boss_come(self,data):
        msg = cmd_s_boss_come()
        msg.ParseFromString( data)
        self.client.log("boss来了")

    def handle_update_score(self,data):
        msg = cmd_s_update_score()
        msg.ParseFromString( data)
        self.client.log("玩家%d现在的钱为%f" % (data.user_id, data.score))

    def handle_roll_msg(self, data):
        msg = cmd_roll_message()
        msg.ParseFromString(data)
        self.client.log("跑马灯:" + msg.message)



#x选择房间
class SelectRoom(BaseCase):

    def __init__(self):
        self.start_user_id = ROBOT_Number #定义测试机器人开始的ID
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        super(DemoCaseJcby, self).__init__()

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





# 金蟾捕鱼-测试用例
class DemoCaseJcby(BaseCase):
    def __init__(self):
        self.start_user_id = ROBOT_Number #定义测试机器人开始的ID
        self.robot_cnt = ROBOT_COUNT  # 定义测试用例测试的假人数量
        super(DemoCaseJcby, self).__init__()

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
        ai_list = super(DemoCaseJcby, self).build_ai(client)

        # 配置登录服务器
        connect_action = ConnectAction(client)
        connect_action.server_ip = SERVER_IP
        connect_action.server_port = SERVER_PORT
        ai_list.add_action(connect_action)

        # 登录
        ai_list.add_action(LoginAction(client))
        ai_list.add_action(SelectRoomAction(client))
        ai_list.add_action(PlayActionJcby(client))
        return ai_list



unit_jcby = DemoCaseJcby()
