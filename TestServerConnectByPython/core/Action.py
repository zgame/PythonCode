# -*- coding: UTF-8 -*-
import time
from Client import *


#登录进游戏等公共行为

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
        self.cur_action = None
        self.action_cnt = 0

    def is_valid(self):
        return len(self.action_list) > 0

    def add_action(self, action):
        if action is None or not isinstance(action, BaseAction) or not action.is_valid():
            return False

        if not action.failed_continue:
            self.failed_continue = False
        self.action_list.append(action)
        self.action_cnt = self.action_list
        return True

    def current_action(self):
        if self.cur_action is not None:
            return self.cur_action
        if not self.is_valid():
            return None
        if self.action_idx >= self.action_cnt:
            return None
        self.cur_action = self.action_list[self.action_idx]
        return self.cur_action

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

        if self.action_idx >= self.action_cnt:
            self.state = ActionState.success
            return True

        action = self.current_action()
        if action is None:
            self.state = ActionState.success
            return True

        if action.is_complete():
            if action.state == ActionState.failed and not action.failed_continue:
                self.state = ActionState.failed
                return True
            else:
                self.action_idx += 1
                self.cur_action = None
                return True
        elif action.state == ActionState.none:
            action.do()
        else:
            action.update()


# 连接登录服务器
class ConnectLsAction(BaseAction):

    def __init__(self, client, timeout=0):
        self.server_ip = ""
        self.server_port = 0
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '连接登录服务器'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务

    def is_conneted_or_conneting(self):
        state = self.client.client_state
        return state == ClientState.connecting_ls or state == ClientState.connected_ls\
            or state == ClientState.logining or state == ClientState.logined \
            or state == ClientState.login_failed

    def do(self):
        if self.is_conneted_or_conneting():
            # self.on_failed("已连接(或正在连接)登录服务器")
            self.client.client_session.disconnect()
            self.client.client_state = ClientState.none
        else:
            self.client.connect_login_server(self.server_ip, self.server_port)
            self.on_begin()

    def update(self):
        if super(ConnectLsAction, self).update():
            return True
        state = self.client.client_state
        if state == ClientState.connected_ls:
            self.on_success()
        return False

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
        if state == ClientState.connected_ls:
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


# 连接聊天服务器
class ConnectChatAction(BaseAction):
    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '连接聊天服务器'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        if len(self.client.chat_server_ip) > 0 and self.client.chat_server_port != 0:
            self.client.connect_chat_server(self.client.chat_server_ip, self.client.chat_server_port)
            self.on_begin()
        else:
            self.on_failed("未获取chatserver服务器,未登录?")

    def update(self):
        if super(ConnectChatAction, self).update():
            return True

        state = self.client.client_state
        if state == ClientState.connected_cs:
            self.on_success()
        return False


# 登录到游戏服务器
class LoginChatAction(BaseAction):

    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '登录聊天服务器'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        state = self.client.client_state
        if state == ClientState.connected_cs:
            self.on_begin()
            self.client.login_cs()
        else:
            self.on_failed("未连接chatserver ?")

    def update(self):
        if super(LoginChatAction, self).update():
            return True
        state = self.client.client_state
        if state == ClientState.logined_cs:
            self.on_success()
        elif state == ClientState.login_failed_cs:
            self.on_failed("")
        return False


# 连接登录服务器
class ConnectGsAction(BaseAction):
    def __init__(self, client, timeout=0):
        self.server_ip = ''
        self.server_port = 0
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '连接游戏服务器'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = True  # 任务失败是否执行下一个任务,用于某些非重要任务

    # 这里简单的随机选择游戏服务器
    def select_game_server(self):
        for server in self.client.gameserver_list:
            if server.min_enter_cannon_lev <= self.client.role_base_info.level:
                self.server_port = server.server_port
                if len(server.server_addr) > 0:
                    idx = random.randint(0, len(server.server_addr) - 1)
                    self.server_ip = server.server_addr[idx]
                    return True
        return False
        '''
        if len(self.client.gameserver_list) > 0:
            idx = random.randint(0, len(self.client.gameserver_list) - 1)
            server = self.client.gameserver_list[idx]
            self.server_port = server.server_port
            if len(server.server_addr) > 0:
                idx = random.randint(0, len(server.server_addr) - 1)
                self.server_ip = server.server_addr[idx]
                return True
        return False
        '''

    def do(self):
        if len(self.client.gameserver_list) > 0:
            if self.select_game_server():
                # self.client.connect_game_server("192.168.101.109", 8301)
                self.client.connect_game_server(self.server_ip, self.server_port)
                self.on_begin()
            else:
                self.on_failed("没有符合的房间?")
        else:
            self.on_failed("未下载gameserver列表,未登录?")

    def update(self):
        if super(ConnectGsAction, self).update():
            return True
        state = self.client.client_state
        if state == ClientState.connected_gs:
            self.on_success()
        return False


# 登录到游戏服务器
class LoginGSAction(BaseAction):

    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '登录游戏服务器'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        state = self.client.client_state
        if state == ClientState.connected_gs:
            self.on_begin()
            self.client.login_gs()
        else:
            self.on_failed("未连接gameserver ?")

    def update(self):
        if super(LoginGSAction, self).update():
            return True
        state = self.client.client_state
        if state == ClientState.logined_gs:
            self.on_success()
        elif state == ClientState.login_failed_gs:
            self.on_failed("")
        return False


# 进入游戏场景
class EnterScenceAction(BaseAction):

    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '进入游戏场景'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务

    def do(self):
        state = self.client.client_state
        if state == ClientState.logined_gs:
            self.on_begin()
            self.client.enter_scence()
        else:
            self.on_failed("未登录gameserver ?")

    def update(self):
        if super(EnterScenceAction, self).update():
            return True
        state = self.client.client_state
        if state == ClientState.entered:
            self.on_success()
        return False


# 玩游戏
class PlayAction(BaseAction):

    def __init__(self, client, timeout=0):
        self.client = client
        self.time_out = timeout  # 超时时间, 0-不超时, 单位: 秒
        self.action_name = '玩游戏'  # 任务名称
        self.state = ActionState.none  # 状态
        self.time_begin = 0  # 任务开始时间
        self.failed_continue = False  # 任务失败是否执行下一个任务,用于某些非重要任务
        self.bullet_cd = 0.2        # 子弹发射间隔
        self.bullet_delay = 1       # 捕获间隔
        self.last_fire_tick = 0     # 上次开炮时间
        self.fish_id = 0            # 锁定鱼ID
        self.select_tick = 0        # 上次选择鱼时间
        self.bullet_id = 1          # 子弹id
        self.bullets = []
        self.failed_cnt = 0         # 失败次数

    def do(self):
        state = self.client.client_state
        if state == ClientState.entered:
            self.on_begin()
        else:
            self.on_failed("当前未进入场景 ?")

    def update(self):
        if super(PlayAction, self).update():
            return True

        if self.client.client_session.state == SessionState.none:
            self.on_failed('disconnect')

        self.do_play()
        return False

    # 选择目标
    def select_fish(self):
        now = time.time()
        # 1s 选择一次
        if now < self.select_tick + 1:
            return

        self.select_tick = now
        if self.fish_id != 0 and self.fish_id in self.client.fish_pool and self.failed_cnt < 10:
            return
        else:
            # pop
            if self.failed_cnt > 10 and self.fish_id != 0 and self.fish_id in self.client.fish_pool:
                self.client.fish_pool.pop(self.fish_id)

            cnt = len(self.client.fish_pool)
            if cnt <= 0:
                self.fish_id = 0
            else:
                self.fish_id = random.choice(self.client.fish_pool.keys())
                self.failed_cnt = 0

    # 开炮,随机方向开炮
    def do_fire(self):
        self.select_fish()
        if self.fish_id == 0:
            return

        cmd = CMD_C_USER_FIRE()
        cmd.tick_count = long(time.time())
        cmd.angle = random.randint(0, 360)
        cmd.lock_fish_id = self.fish_id
        cmd.bullet_mulriple = 1
        cmd.bullet_temp_id = self.bullet_id
        self.bullet_id += 1
        cmd.bullet_num = 1
        cmd.is_broadcast = True
        bullet = BulletObj()
        bullet.bullet_id = cmd.bullet_temp_id
        bullet.tick = cmd.tick_count
        bullet.fish_id = cmd.lock_fish_id
        # self.bullets.append(bullet)
        s = cmd.SerializeToString()
        self.failed_cnt += 1
        self.client.fire_cnt += 1
        self.client.client_session.send_data(MDM_GF_GAME, SUB_C_USER_FIRE, s)
        # self.client.log("fire fish:%d!" % cmd.lock_fish_id)

    # 捕获
    def do_catch(self, bullet):
        cmd = CMD_C_CATCH_FISH()
        cmd.fish_uid = bullet.fish_id
        cmd.bullet_id = bullet.bullet_id
        cmd.bullet_temp_id = bullet.bullet_local_id
        cmd.chair_id = self.client.chair_id
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MDM_GF_GAME, SUB_C_CATCH_FISH, s)

    # 模拟游戏逻辑
    def do_play(self):
        tm_now = time.time()
        if tm_now > self.last_fire_tick + self.bullet_cd:
            self.last_fire_tick = tm_now
            self.do_fire()

    # 处理子弹消息,将自己的子弹加入列表,以便捕获到鱼
    # 其它人的子弹忽略
    def handle_user_fire(self, data):
        msg = CMD_S_USER_FIRE()
        msg.ParseFromString(data)
        # 自己发射的子弹
        if msg.chair_id == self.client.chair_id:
            bullet = BulletObj()
            bullet.bullet_id = msg.bullet_id
            bullet.fish_id = msg.lock_fish_id
            bullet.bullet_local_id = msg.bullet_temp_id
            bullet.tick = time.time()
            # 添加到本地子弹列表
            # self.bullets.append(bullet)
            # 更新当前金币数量
            self.client.role_base_info.score = msg.curr_score
            self.do_catch(bullet)
            # self.client.log("fire success:fish:%d!" % bullet.fish_id)

    def handle_catch_fish(self, data):
        msg = CMD_S_CATCH_FISH()
        msg.ParseFromString(data)
        catch_cnt = 0
        total_score = 0
        self.fish_id = 0
        mine = (msg.chair_id == self.client.chair_id)
        for fish in msg.catch_fishs:
            if fish.fish_uid in self.client.fish_pool:
                self.client.fish_pool.pop(fish.fish_uid)
            catch_cnt += 1
            total_score += fish.fish_score
        if mine:
            self.failed_cnt = 0
            self.client.role_base_info.score = msg.curr_score
            self.client.catch_cnt += 1
            self.client.log("捕获到%d条鱼,获得金币:%d,经验:%d" % (catch_cnt, total_score, msg.add_exp))

    def handle_draw_alm(self, data):
        cmd = CMD_C_GET_ALMS()
        s = cmd.SerializeToString()
        self.client.client_session.send_data(MDM_GF_GAME, SUB_C_GET_ALMS, s)

    # 处理网络消息处理
    def handle_net_msg(self, msg):
        msg_id = msg.msg_id
        sub_msg_id = msg.sub_msg_id

        if msg_id == MDM_GF_GAME:
            if sub_msg_id == SUB_S_USER_FIRE:
                self.handle_user_fire(msg.data)
            elif sub_msg_id == SUB_S_CATCH_FISH:
                self.handle_catch_fish(msg.data)
            elif sub_msg_id == SUB_S_START_ALMS:
                self.handle_draw_alm(msg.data)
