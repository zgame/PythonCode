# -*- coding: UTF-8 -*-


# 简单,数据加密解密,按位与
import binascii


class SimpleEncrypt(object):

    # 加密
    # @param data: string 类型
    @staticmethod
    def encrypt(s):
        lst = []
        length = len(s)
        for i in range(length):
            tmp = length-i
            c = ord(s[i])
            c ^= 0xE9 * tmp + tmp % 14
            lst.append(chr(c % 256))
        return ''.join(lst)

    # 解密
    # @param data: string 类型
    @staticmethod
    def decrypt(s):
        return SimpleEncrypt.encrypt(s)
