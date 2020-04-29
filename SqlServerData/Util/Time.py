import time


# 时间字符串变时间戳
def get_time_stamp(time_str):
    time_array = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    # print(time_array)
    time_stamp = int(time.mktime(time_array))
    return time_stamp


# 时间戳变更时间字符串
def get_time_string(stamp):
    time_array = time.localtime(stamp)
    re_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    # print(re_time)  # 2013--10--10 23:40:00
    return re_time


# 测试
print(get_time_string(1452176113))
print(get_time_string(time.time()))
print(get_time_stamp("2020-01-09 00:00:00"))
print(get_time_stamp("2020-01-10 00:00:00"))
