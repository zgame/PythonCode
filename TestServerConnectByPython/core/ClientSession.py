# -*- coding: UTF-8 -*-
import random
import socket
import time
import select
from errno import *

from core.Encrypt import SimpleEncrypt
from core.NetWork import *

WORK_THREAD_CNT = 8

class SessionState(object):
    none = 0
    wait_connect = 1
    connecting = 2
    connected = 3


class ServerType(object):
    none = 0
    login_server = 1
    game_server = 2
    chat_server = 3


class ClientSession(object):

    def __init__(self):
        self.client = None
        self.server_ip = ""
        self.server_port = 0
        self.state = SessionState.none
        self.servertype = ServerType.none
        self.token_id = 0  # 包序号
        self.readbuf = ''
        self.send_msg_queue = NetMsgQueue('send')
        self.recv_msg_queue = NetMsgQueue('recv')
        self.sock = None

        self.total_cnt = 0
        self.total_cost = 0.0
        self.max_cost = 0.0

    def connect_login_server(self, ip, port):
        if self.is_connected():
            self._disconnect()

        self.server_ip = ip
        self.server_port = port
        self.servertype = ServerType.login_server
        self._connect()

    def connect_game_server(self, ip, port):
        if self.is_connected():
            self.disconnect()

        self.server_ip = ip
        self.server_port = port
        self.servertype = ServerType.game_server
        self._connect()

    def connect_chat_server(self, ip, port):
        if self.is_connected():
            self.disconnect()

        self.server_ip = ip
        self.server_port = port
        self.servertype = ServerType.chat_server
        self._connect()

    def is_connected(self):
        return self.state == SessionState.connected

    def _connect(self):
        if self.sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.state = SessionState.wait_connect

    def disconnect(self):
        self.state = SessionState.none
        # self.sock.shutdown(socket.SHUT_WR)
        # self.sock.close()
        self.sock = None
        self.send_msg_queue.clear()
        self.recv_msg_queue.clear()

    def on_connect_failed(self, err):
        self.state = SessionState.none
        self.client.log("连接[%s:%d]失败,错误码:%d" % (self.server_ip, self.server_port, err))

    def on_connect_success(self):
        self.state = SessionState.connected
        self.token_id = 0
        self.sock.setblocking(0)
        if self.servertype == ServerType.login_server:
            self.client.on_loginsvr_connect()
        elif self.servertype == ServerType.game_server:
            self.client.on_gamesvr_connect()
        else:
            self.client.on_chatsvr_connect()

    def on_disconnect(self, err):
        self.client.log("连接[%s:%d]已断开:%d" % (self.server_ip, self.server_port, err))
        self.disconnect()

    def on_socket_err(self, err):
        if err == 10054:
            self.on_disconnect(err)
        else:
            self.client.log("on_socket_err:%d" % err)

    def debug_msg(self, msg):
        cnt = self.send_msg_queue.size()
        if cnt > 100:
            self.client.log(msg)
            self.client.log("queue size:%d" % cnt)

    def send_data(self, msgid, subid, data):
        if self.state != SessionState.connected:
            return

        msg = NetMsg()
        msg.msg_id = msgid
        msg.sub_msg_id = subid
        msg.token_id = self.token_id
        self.token_id += 1
        msg.data = data
        self.send_msg_queue.push(msg)
        # self.debug_msg("push net msg")

    def on_update(self):
        self.client.update()

        if self.sock is None:
            return

        if self.state == SessionState.wait_connect:
            self.state = SessionState.connecting
            err = self.sock.connect_ex((self.server_ip, self.server_port))
            if err == 0 or err == 10056:  # 10056 已连接
                self.on_connect_success()
            elif err == WSAEWOULDBLOCK:  # 10035 wsaewouldblock, 异步
                self.state = SessionState.wait_connect
            else:
                self.on_connect_failed(err)
            return

        if not self.is_connected():
            return

        tm_begin = time.time()
        try:
            keys = [self.sock]
            rlist, wlist, elist = select.select(keys, keys, keys, 0.000001)
            if len(rlist) > 0:
                self.on_read()
            if len(wlist) > 0:
                self.on_write()
            if len(elist) > 0:
                self.on_exceiption()
        except Exception, e:
            print e
        tm_span = time.time() - tm_begin
        self.total_cost += tm_span
        self.total_cnt += 1
        if tm_span > self.max_cost:
            self.max_cost = tm_span
        # if self.total_cnt % 100 == 0:
        #    print 'avr cost:%f, max cost:%f' % (self.total_cost/self.total_cnt, self.max_cost)

    # 从接收数据队列解析数据包
    def parse_packet(self):
        while len(self.readbuf) >= TcpHead.length():

            # print("receive buffer:",self.readbuf)
            head = TcpHead()
            head.unpacket(self.readbuf[0:10])
            offset = head.length()
            data_len = head.packet_size
            if head.pack_ver > 0:
                if len(self.readbuf) < TcpHeadNew.length() + data_len:
                    return
                offset = TcpHeadNew.length()
            else:
                if len(self.readbuf) < head.length() + data_len:
                    return
            data = self.readbuf[offset:offset+data_len]
            self.readbuf = self.readbuf[offset + data_len:]
            msg = NetMsg()
            msg.msg_id = head.msg_id
            msg.sub_msg_id = head.sub_msg_id
            msg.data = data
            self.recv_msg_queue.push(msg)

    # 接收数据
    def on_read(self):
        if not self.is_connected():
            return

        try:
            data = self.sock.recv(8192)
            if not data or len(data) == 0:
                self.on_disconnect(0)
                return
            else:
                self.readbuf = self.readbuf + data
                self.parse_packet()
        except socket.error, se:
            no = se.args[0]
            if no in (EAGAIN, WSAEINTR, WSAEWOULDBLOCK):
                return
            else:
                self.on_socket_err(no)

    # 发送一个数据包
    def _inner_send(self, msg):
        head = TcpHead()
        data = SimpleEncrypt.encrypt(struct.pack('H', msg.token_id) + msg.data)
        head.packet_size = len(data)
        head.msg_id = msg.msg_id
        head.sub_msg_id = msg.sub_msg_id
        head.pack_ver = 1
        head.token_id = msg.token_id

        buf = head.packet() + data
        total_send_cnt = 0
        total_len = len(buf)

        # print("-----------------------------")
        # print("send buffer :", buf)

        while total_send_cnt < total_len:
            try:
                send_cnt = self.sock.send(buf[total_send_cnt:])
                if send_cnt == 0:
                    self.on_disconnect(0)
                    return False
                else:
                    total_send_cnt += send_cnt
            except socket.error, se:
                no = se.args[0]
                if no in (EAGAIN, WSAEINTR, WSAEWOULDBLOCK):
                    self.client.log("send WSAEWOULDBLOCK error: %d" % no)
                    return False
                else:
                    self.on_socket_err(no)
                    return False
        return True

    def on_write(self):
        if self.send_msg_queue.empty():
            return
        cnt = 0
        while not self.send_msg_queue.empty() and cnt < 3:
            msg = self.send_msg_queue.peek()
            if msg is None:
                return
            if self._inner_send(msg):
                self.send_msg_queue.pop()
                cnt += 1
                # self.debug_msg("send on net msg")
            else:
                break

    def on_exceiption(self):
        pass


class WorkThread(object):
    def __init__(self):
        self.running = True
        self.lock = threading.RLock()
        self.sessions = []
        self.thread = threading.Thread(target=self.work_proc)
        self.thread.setDaemon(True)
        self.thread.start()

    def stop(self):
        self.running = False

    def bind_session(self, session):
        self.lock.acquire()
        self.sessions.append(session)
        self.lock.release()

    def work_proc(self):
        while self.running:
            if len(self.sessions) == 0:
                time.sleep(0.1)
                continue

            time_begin = time.time()
            # print 'session cnt:%d' % len(self.sessions)
            # 用于检查连接等
            for ss in self.sessions:
                ss.on_update()

            if time.time() - time_begin < 0.01:
                time.sleep(0.01)


# 管理Session,并维护Session状态
class SessionManager(object):

    def __init__(self):
        self.threads = []       # 工作线程

    def _init_work_thread(self):
        for i in range(WORK_THREAD_CNT):
            self.threads.append(WorkThread())

    # 创建Session并分配工作线程
    def new_session(self):
        if len(self.threads) == 0:
            self._init_work_thread()
        session = ClientSession()
        idx = random.randint(0, WORK_THREAD_CNT - 1)
        thread = self.threads[idx]
        thread.bind_session(session)
        return session


G_SessionMgr = SessionManager()
