#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口好
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))


msg = '我来了！' + "\r\n"
s.send(msg.encode('utf-8'))
# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print (msg.decode('utf-8'))


# 跟C服务器的数据格式同步问题
import struct

# native byteorder
buffer = struct.pack("BBHHHH", 0, 1, 0, 1100, 3, 0)
print(buffer)
print(struct.unpack("BBHHHH", buffer))
# data from a sequence, network byteorder
data = [0, 1, 0, 1100, 10, 0]
buffer = struct.pack("!BBHHHH", *data)
print(repr(buffer))
print(struct.unpack("!BBHHHH", buffer))

