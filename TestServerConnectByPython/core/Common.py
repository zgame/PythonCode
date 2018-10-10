# -*- coding: UTF-8 -*-


# 访客数据对象
import ctypes
from ctypes import wintypes

import struct


class GuestInfo(object):
    def __init__(self):
        self.machine_id = ""             # 机器码
        self.ditch_id = 9                # 渠道号
        self.client_type = 3             # 客户端类型: 1为网页 2为PC 3为IOS 4为android
        self.client_kind = 3             # 游戏id
        self.game_kind = 8               # 游戏类型: 1 - 满贯推币机；2 - 满贯猜正反； 3 - 满贯捕鱼
        self.client_version = 0          # 客户端版本号
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

    # mac = "74-D4-36-AD-36-18"
    return mac
