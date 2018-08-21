import time
import tkinter.messagebox as msgbox
from tkinter import *
import iniparser

list_select_index_all = 0
label_list = []


class Room:
    cpu = 0
    memory = 0
    io_read = 0
    io_write = 0
    online = 0
    state = 0

    def __init__(self, name, id, time):
        self.name = str(name, encoding='gb2312')
        # self.name = name
        self.id = id
        self.start_time = time


Room_Info_list = []
list_all = None


def open_ui(room_list):
    if len(room_list) == 0:
        return

    for ro in room_list:
        room_t = Room(ro.server_name, ro.server_id, ro.start_time)
        Room_Info_list.append(room_t)

    row_t = 0
    root = Tk()

    # --------title-----------------------------
    root.title("Tools" + "  _Version: v1.02")
    # -------添加label---------------------------------------------------------
    frame_left = Frame(root)
    frame_left.grid(row=row_t, rowspan=3, column=0, columnspan=1, sticky=W + E)

    frame_right = Frame(root)
    frame_right.grid(row=row_t, rowspan=3, column=3, columnspan=2, sticky=W + E)

    label = Label(frame_left, text="双击选择服务器列表...", font=("微软雅黑", 12))
    label.grid(row=row_t, column=0, columnspan=2, sticky=W)
    from MonitorClient import send_gm_cmd
    """GM
  #     KickALLUser
  #     RoomClose
  #     RoomOpen """

    # ---------------------踢所有玩家----------------------------------
    def tips():
        # if Room_Info_list[list_select_index_all].name == "登录服务器" or Room_Info_list[list_select_index_all].name == "中心服务器":
        #     msgbox.showinfo("提示", "只能控制游戏服务器!")
        #     return 1
        return 0

    def kick_all_user():
        if not tips():
            # 遍历所有选择的服务器
            for item in list_all.curselection():
                room_id = Room_Info_list[item].id
                send_gm_cmd(room_id, "@KickALLUser")

    # ---------------------房间维护---------------------
    def list_room_off():
        if not tips():
            for item in list_all.curselection():
                room_id = Room_Info_list[item].id
                send_gm_cmd(room_id, "@RoomClose")

    # ---------------------停止维护---------------------
    def list_room_on():
        if not tips():
            for item in list_all.curselection():
                room_id = Room_Info_list[item].id
                send_gm_cmd(room_id, "@RoomOpen")

    # ---------------------通知玩家维护---------------------
    def notice_all_user():
        if not tips():
            for item in list_all.curselection():
                room_id = Room_Info_list[item].id
                send_gm_cmd(room_id, "@NoticeAllUser")

    # ---------------------refresh_ip_list---------------------
    def refresh_ip_list():
        if not tips():
            for item in list_all.curselection():
                room_id = Room_Info_list[item].id
                send_gm_cmd(room_id, "@RefreshIpList")

    # ---------------------send_rank_award---------------------
    def send_rank_award():
        # for item in list_all.curselection():
        room_id = Room_Info_list[list_select_index_all].id
        conf = iniparser.INIParser()
        conf.read("Setting.ini")
        root = conf.get_section("author")
        str_t = "@SendRankAward " + str(root.get("rankID")) + " " + root.get("timeStart") + " " + root.get("timeEnd")
        print(str_t)
        room_id = '-100'
        send_gm_cmd(room_id, str_t)

    # ---------------添加控制按钮----------------------------------
    row_t = 0
    button = Button(frame_right, text='房间维护', command=list_room_off)
    button.grid(row=row_t, column=1, sticky=W + E + S + N)
    row_t = row_t + 1
    button = Button(frame_right, text='停止维护', command=list_room_on)
    row_t = row_t + 1
    button.grid(row=row_t, column=1, sticky=W + E + S + N)
    button = Button(frame_right, text='踢所有玩家', command=kick_all_user)
    row_t = row_t + 1
    button.grid(row=row_t, column=1, sticky=W + E + S + N)
    button = Button(frame_right, text='通知玩家 5min后自动踢人', command=notice_all_user)
    row_t = row_t + 1
    button.grid(row=row_t, column=1, sticky=W + E + S + N)
    button = Button(frame_right, text='刷新ip白名单', command=refresh_ip_list)
    row_t = row_t + 1
    button.grid(row=row_t, column=1, sticky=W + E + S + N)
    button = Button(frame_right, text='中心服发排行奖励', command=send_rank_award)
    row_t = row_t + 1
    button.grid(row=row_t, column=1, sticky=W + E + S + N)

    # row_t = row_t + 6

    row_t = row_t + 1

    # 通过双击获取当前选择的房间设置index
    def print_cur_list(event):
        global list_select_index_all
        list_select_index_all = list_all.curselection()[0]
        refresh_show()

    all_room_setting_list = []
    for item_room in Room_Info_list:
        # name = str(item_room.name, encoding='gb2312')
        name = item_room.name
        all_room_setting_list.append(name)

    global list_all
    list_all = Listbox(frame_left, height=35, width=55, selectmode=EXTENDED)
    for item in all_room_setting_list:
        list_all.insert(END, item)

    list_all.bind('<Double-Button-1>', print_cur_list)
    list_all.grid(row=row_t, column=0, columnspan=3, sticky=W + E + N + S)

    # --------滚动条-----------------------
    sl = Scrollbar(frame_left)
    sl.config(command=list_all.yview)
    sl.grid(row=row_t, column=3, sticky=W + S + N)
    list_all.config(yscrollcommand=sl.set)

    # 操作说明
    # fr = Frame(root)
    # fr.grid(row=row_t, column=0, sticky=W+E+S+N)
    label = Label(frame_right, text="操作说明：")
    label.grid(row=row_t, column=0, sticky=W + E + S + N)
    label = Label(frame_right, text="1.列表支持多选，ctrl键控制不连续内容选择，")
    label.grid(row=row_t + 1, column=0, sticky=W + E + S + N)
    label = Label(frame_right, text="Shift键为连续选择，支持鼠标按住多个连续选择。")
    label.grid(row=row_t + 2, column=0, sticky=W + E + S + N)
    label = Label(frame_right, text="2. 只能选择游戏服务器")
    label.grid(row=row_t + 3, column=0, sticky=W + E + S + N)
    label = Label(frame_right, text="3.注意这里的服务器人数是指包含机器人的数量，所以踢不干净是因为有机器人在里面")
    label.grid(row=row_t + 4, column=0, sticky=W + E + S + N)
    label = Label(frame_right, text="4. ")
    label.grid(row=row_t + 5, column=0, sticky=W + E + S + N)

    # --------------------------------------------------------------------------------
    # ---------选择房间和机器人的下拉按钮-----------------------------------------------------------------
    # --------------------------------------------------------------------------------
    row_t = row_t + 1
    frame_down = Frame(root)
    frame_down.grid(row=row_t, column=0, columnspan=1, sticky=W + E + N + S)
    frame_downt2 = Frame(root)
    frame_downt2.grid(row=row_t, column=2, columnspan=3, sticky=W + E)

    global label_list

    label_list.append(Label(frame_down, text="房间的id: "))
    label_list[0].grid(row=row_t, column=0, sticky=W)

    label_list.append(Label(frame_downt2, text="运行时间: "))
    label_list[1].grid(row=row_t, column=3, sticky=W)

    row_t = row_t + 1
    label_list.append(Label(frame_down, text="cpu: "))
    label_list[2].grid(row=row_t, column=0, sticky=W)

    label_list.append(Label(frame_downt2, text="online: "))
    label_list[3].grid(row=row_t, column=3, sticky=W)

    row_t = row_t + 1
    label_list.append(Label(frame_down, text="io_read: "))
    label_list[4].grid(row=row_t, column=0, sticky=W)

    label_list.append(Label(frame_downt2, text="io_write: "))
    label_list[5].grid(row=row_t, column=3, sticky=W)

    row_t = row_t + 1
    label_list.append(Label(frame_down, text="memory: "))
    label_list[6].grid(row=row_t, column=0, sticky=W)

    label_list.append(Label(frame_downt2, text="state: "))
    label_list[7].grid(row=row_t, column=3, sticky=W)

    root.mainloop()


def refresh_show():
    label_list[0].config(text="房间的id: " + str(Room_Info_list[list_select_index_all].id))
    time_t = time.time() - Room_Info_list[list_select_index_all].start_time
    time_t = round(time_t / (60 * 60), 2)
    label_list[1].config(text="运行时间: " + str(time_t) + "小时")

    label_list[2].config(text="cpu: " + str(Room_Info_list[list_select_index_all].cpu) + "%")
    label_list[3].config(text="online: " + str(Room_Info_list[list_select_index_all].online) + "人（包含机器人）")
    mem = round(Room_Info_list[list_select_index_all].io_read / (1024 * 1024), 2)
    label_list[4].config(text="io_read: " + str(mem) + "M")
    mem = round(Room_Info_list[list_select_index_all].io_write / (1024 * 1024), 2)
    label_list[5].config(text="io_write: " + str(mem) + "M")

    mem = round(Room_Info_list[list_select_index_all].memory / (1024 * 1024), 2)
    label_list[6].config(text="memory: " + str(mem) + "M")

    label_list[7].config(text="state: " + str(Room_Info_list[list_select_index_all].state))


# 网络回来的数据，用来做数据刷新
def refresh_server_list_info(server_info):
    for (index, room) in enumerate(Room_Info_list):
        if room.id == server_info.server_id:
            room.id = server_info.server_id
            room.cpu = server_info.cpu
            room.memory = server_info.memory
            room.io_read = server_info.io_read
            room.io_write = server_info.io_write
            room.online = server_info.online
            if room.state != server_info.room_state:
                # 服务器状态发生变化了
                room.state = server_info.room_state
                global list_all
                list_all.delete(index, index)
                list_all.insert(index, get_room_name(room.name, room.state))
    refresh_show()


def get_room_name(name, state):
    if state == 1:
        return name + "     --房间维护中"
    return name


# 建立一个服务器的大列表
def refresh_server_list_name(room_list):
    Room_Info_list.clear()
    for ro in room_list:
        room_t = Room(ro.server_name, ro.server_id, ro.start_time)
        Room_Info_list.append(room_t)


# 新增一个服务器房间
def add_server_list(add_room):
    room_t = Room(add_room.item.server_name, add_room.item.server_id, add_room.item.start_time)
    Room_Info_list.append(room_t)

    global list_all
    list_all.insert(END, room_t.name)


# del一个服务器房间
def del_server_list(room):
    for (index, ro) in enumerate(Room_Info_list):
        if ro.id == room.server_id:
            Room_Info_list.remove(ro)
            global list_all
            list_all.delete(index, index)
