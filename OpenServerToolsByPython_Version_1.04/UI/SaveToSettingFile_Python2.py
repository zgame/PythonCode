# coding=utf-8

# 将临时修改的roomlist保存到文件中


def save_to_file(list):
    file = 'Setting/SettingRooms.py'
    # -----1 保留文件的前面的信息------------
    file_data = ""
    with open(file, 'r') as f:
        for line in f:
            if "room_list" in line:
                break
            file_data += line
    # -----2 处理新的list------------
    # 2.1 先处理新增加的每个行， 拼在一起
    all_line_data = ""
    for item in list:
        str_t = example_line_str % (item.ServerID, item.ServerName, item.ServerMachine, item.AndroidCount, item.GameRoomListIndex, item.SqlFileRobotListIndex)
        all_line_data = all_line_data + str_t       # 把所有行组合在一起

    # 2.2 把数据插入到格式中
    all_line_data = example_list_str % all_line_data

    file_data = file_data + all_line_data

    # ----3 开始保存----------
    with open(file, "w") as f:
        f.write(file_data)

    # ---4 测试一下----------
    with open(file, 'r') as f:
        re = f.read()
    print(re)



example_list_str = """room_list = [
    # 要配置的房间的信息， 可以一次性配置N多房间， 在列表后面增加即可
    #          房间的ID    房间名字        端口号        机器码      机器人的数量  要创建房间类型的编号   要加入机器人的sql编号
    %s
]
"""

example_line_str = """RoomSetting("%s", "%s", "作废了", "%s",    %s,             %s,                  %s),
"""

# ----------------------------------------------------------------------------------------------
# --------------根据python版本不同的接口----------------------------------------------------------
# ----------------------------------------------------------------------------------------------

def zsw_python2_python3_unicode_str(txt):
    return unicode(txt, "utf-8")
    # return str(txt, "utf-8")