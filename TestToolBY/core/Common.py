# -*- coding: UTF-8 -*-


# 访客数据对象
import ctypes
from ctypes import wintypes

import struct


class GuestInfo(object):
    def __init__(self):
        self.user_id = 0                 # user_id
        self.token = ""                  # token
        self.machine_id = ""             # 机器码
        self.ditch_id = 1                # 渠道号
        self.plat_kind = 2               # 客户端类型:  0-未知/网页，1-平台App,2-满贯内嵌
        self.game_kind = 100
        self.client_kind = 3             # 游戏id
        self.client_version = 1          # 客户端版本号
        self.client_type = 1             # 设备系统类型
        self.ip_address = ""             # ip地址
        self.device_type = "virtual"     # 设备的型号


# 鱼对象
class FishObj(object):
    def __init__(self):
        self.uid = 0
        self.kind_id = 0
        self.tick = 0


# 子弹对象
class BulletObj(object):
    def __init__(self):
        self.bullet_local_id = 0        # 本地id
        self.bullet_id = 0              # 服务器id
        self.tick = 0                   # 发射时间
        self.fish_id = 0                # 锁定鱼id


# 利用栈对象原则,自动解锁
class AutoLock(object):
    def __init__(self, lock):
        self.lock = lock
        if self.lock:
            self.lock.acquire()

    def __del__(self):
        if self.lock:
            self.lock.release()


def dump_memory(src):
    length = len(src)
    print("Dump Memory: %d Bytes:\n", length)
    dest = ''
    for i in range(length):
        dest += "%2x " % ord(src[i])
    print dest


def build_mac_addr(num):
    buf = struct.pack('Q', num)
    hex_lst = []
    for i in range(6):
        hex_lst.append('00')
    idx = 0
    for e in buf:
        hex_lst[6-idx-1] = hex(ord(e))
        idx += 1
        if idx >= 6:
            break
    mac = '-'.join(hex_lst).replace('0x', '').upper()
    return mac
