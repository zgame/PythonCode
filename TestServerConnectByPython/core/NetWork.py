# -*- coding: UTF-8 -*-
import struct
import threading
from Common import *


class TcpHead(object):

    def __init__(self):
        self.data_kind = 0  # byte
        self.check_code = 1  # byte
        self.packet_size = 0  # word
        self.msg_id = 0  # word
        self.sub_msg_id = 0  # word
        self.pack_ver = 0  # word

    def packet(self):
        buf = struct.pack('cchhhh', chr(self.data_kind), chr(self.check_code), self.packet_size,
                          self.msg_id, self.sub_msg_id, self.pack_ver)

        # print ("head byte :", buf)
        return buf

    def unpacket(self, buf):
        self.data_kind, self.check_code, self.packet_size, self.msg_id, self.sub_msg_id, \
            self.pack_ver = struct.unpack('cchhhh', buf)
        # print(" receive :", buf)

    @staticmethod
    def length():
        return 10


class TcpHeadNew(object):
    def __init__(self):
        self.data_kind = 0  # byte
        self.check_code = 1  # byte
        self.packet_size = 0  # word
        self.msg_id = 0  # word
        self.sub_msg_id = 0  # word
        self.pack_ver = 0  # word
        self.token_id = 0  # word

    def packet(self):
        buf = struct.pack('cchhhhh', chr(self.data_kind), chr(self.check_code), self.packet_size,
                          self.msg_id, self.sub_msg_id, self.pack_ver, self.token_id)
        return buf

    def unpacket(self, buf):
        self.data_kind, self.check_code, self.packet_size, self.msg_id, self.sub_msg_id, \
        self.pack_ver, self.token_id = struct.unpack('cchhhhh', buf)

    @staticmethod
    def length():
        return 12


# 网络消息
class NetMsg(object):
    def __init__(self):
        self.msg_id = 0
        self.sub_msg_id = 0
        self.token_id = 0
        self.data = []


# 消息队列
class NetMsgQueue(object):
    def __init__(self, name=''):
        self.lock = threading.RLock()
        self.elements = []
        self.name = name

    # 是否为空
    def empty(self):
        return len(self.elements) == 0

    # 取当前大小
    def size(self):
        AutoLock(self.lock)
        return len(self.elements)

    # 加入队列
    def push(self, element):
        AutoLock(self.lock)
        self.elements.append(element)
        # if len(self.elements) >= 50:
        #     print 'element [%s,%d,%d,%d] cnt %d' % (self.name, id(self), element.msg_id, element.sub_msg_id,
        #                                             len(self.elements))

    # 取队列首个,但不出队列
    def peek(self):
        AutoLock(self.lock)
        if len(self.elements) > 0:
            return self.elements[0]
        return None

    # 取队首
    def pop(self):
        AutoLock(self.lock)
        if len(self.elements) > 0:
            elm = self.elements.pop(0)
            return elm
        return None

    # 清除队列
    def clear(self):
        AutoLock(self.lock)
        self.elements = []
