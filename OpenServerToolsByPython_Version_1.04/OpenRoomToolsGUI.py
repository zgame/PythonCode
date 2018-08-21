# coding=utf-8
# ---------------python 3.6-------------------------------------------------------
# from tkinter import *
# import tkinter.messagebox as msgbox
# import tkinter.filedialog as fd
# from UI.SaveToSettingFile_Python3 import save_to_file
# ---------------python 2.7-------------------------------------------------------
from Tkinter import *
import tkFileDialog as fd
from UI.SaveToSettingFile_Python2 import save_to_file
import tkMessageBox as msgbox
# -------------------------------------------------------

from Setting.SettingRooms import room_list
from Setting.SettingSQL import SqlFiles, NewGameRoomSql, Versions
import copy
from Scripts.Run import main as mt
from Scripts.Run import CheckSqlServerIdDuplicate

list_select_index_all = 0   # 房间数据的选择
list_select_index1 = 0      # 房间类型的选择
list_select_index2 = 0      # 机器人的选择
list_select_index3 = 0      # 版本号的选择

def main():
    row_t = 0
    root = Tk()

    # --------title-----------------------------
    root.title("Tools")
    # -------添加label---------------------------------------------------------
    frame_t = Frame(root)
    frame_t.grid(row=row_t, rowspan=6, column=0,  columnspan=1, sticky=W+E)

    frame_right = Frame(root)
    frame_right.grid(row=row_t, rowspan=6, column=2,  columnspan=4, sticky=W+E)

    label = Label(frame_t, text="双击！双击！选择对应的数据...", font=("微软雅黑", 12))
    label.grid(row=row_t, column=0, columnspan=2, sticky=W)

    # ---------------------添加房间----------------------------------
    def list_add():
        global list_select_index_all
        # 指定到最新添加的地方
        list_select_index_all = list_all.size()-1

        rs = copy.deepcopy(room_list[len(room_list)-1])
        rs.ServerID = str(int(rs.ServerID) + 1)
        room_list.append(rs)
        list_all.insert(END, rs.ServerID)           # listBox 添加显示

        index = list_all.size()-1             # 添加到最后的位置
        picks0.add_command(label=rs.ServerID, command=lambda index=index: select_cur_list(index))         # menubutton添加显示

        refresh_data()

    # ---------------------删除列表---------------------
    def list_del():
        global list_select_index_all
        if list_all.size() > 1:
            room_list.pop(list_select_index_all)
            list_all.delete(list_select_index_all, list_select_index_all)

            # 这里注意一下， 菜单按钮绑定的是index，所以，删除之后，重置一遍index
            picks0.delete(0, END)
            for (index, value) in enumerate(room_list):
                picks0.add_command(label=value.ServerID, command=lambda index=index: select_cur_list(index))

            # 光标往上
            list_select_index_all = list_select_index_all - 1

            # 如果还有元素，那么刷新一下
            if list_all.size() > 0:
                refresh_data()
        else:
            msgbox.showinfo("提示","至少要留一个房间作为copy的模板！")

    # ---------------------保存到文件中---------------------
    def list_save():
        # 首先要保存当前的数据

        # 如果变更了server id，需要刷新一下
        input_server_id = input1.get().encode("utf-8")
        if room_list[list_select_index_all].ServerID != input_server_id:
            # 更新listbox
            list_all.delete(list_select_index_all)
            list_all.insert(list_select_index_all, input_server_id)
            # 更新menubutton
            mbutton0.config(text=input_server_id)

        room_list[list_select_index_all].ServerID = input_server_id
        room_list[list_select_index_all].ServerName = input2.get().encode("utf-8")
        room_list[list_select_index_all].AndroidCount = input3.get().encode("utf-8")
        room_list[list_select_index_all].ServerMachine = input4.get().encode("utf-8")
        room_list[list_select_index_all].GameRoomListIndex = list_select_index1
        room_list[list_select_index_all].SqlFileRobotListIndex = list_select_index2

        # 用当前的版本号，把所有的版本号都同步一遍
        for item in room_list:
            re = item.ServerName.split("_")
            item.ServerName = re[0] + "_" + Versions[list_select_index3]


        # 然后把数据保存到文件中
        save_to_file(room_list)

    # ---------------添加控制按钮----------------------------------
    button = Button(frame_t, text='新增', command=list_add)
    button.grid(row=row_t, column=3, sticky=W)
    button = Button(frame_t, text='删除', command=list_del)
    button.grid(row=row_t, column=4)
    button = Button(frame_t, text='保存', command=list_save)
    button.grid(row=row_t, column=5)

    row_t = row_t + 6

    # --------------------------------------------------------------------------------
    # -------添加listBox---------------------------------------------------------
    # --------------------------------------------------------------------------------
    # 通过双击获取当前选择的房间设置index
    def print_cur_list(event):
        global list_select_index_all
        list_select_index_all = list_all.curselection()[0]
        refresh_data()

    all_room_setting_list = []
    for item_room in room_list:
        id = item_room.ServerID
        if CheckSqlServerIdDuplicate(id) == 1:
            # 重复了，要提示
            id = item_room.ServerID + "重复了！"
        all_room_setting_list.append(id)

    list_all = Listbox(frame_t, height=10, width=25, selectmode=SINGLE)
    for item in all_room_setting_list:
        list_all.insert(END, item)

    list_all.bind('<Double-Button-1>', print_cur_list)
    list_all.grid(row=row_t, column=0, columnspan=3, sticky=W + E + N + S)

    # --------滚动条-----------------------
    sl = Scrollbar(frame_t)
    sl.config(command=list_all.yview)
    sl.grid(row=row_t, column=3, sticky=W + S + N)
    list_all.config(yscrollcommand=sl.set)

    # 操作说明
    # fr = Frame(root)
    # fr.grid(row=row_t, column=0, sticky=W+E+S+N)
    label = Label(frame_right, text="操作说明：" )
    label.grid(row=row_t, column=0, sticky=W+E+S+N)
    label = Label(frame_right, text="1.该工具为配置文件修改工具，双击列表或者下拉")
    label.grid(row=row_t+1, column=0, sticky=W+E+S+N)
    label = Label(frame_right, text="按钮选择要编辑的房间，编辑完成后记得点击保存！" )
    label.grid(row=row_t+2, column=0, sticky=W+E+S+N)
    label = Label(frame_right, text="2. 任何房间的改动都要先保存，不点保存，配置文件不变！")
    label.grid(row=row_t+3, column=0, sticky=W+E+S+N)
    label = Label(frame_right, text="3. 可查看输出信息。可手动改配置文件，再Run.py也可开服！")
    label.grid(row=row_t+4, column=0, sticky=W+E+S+N)
    label = Label(frame_right, text="4. 同一个版本号的房间要一起开服！")
    label.grid(row=row_t+5, column=0, sticky=W+E+S+N)

    # ---------一个菜单按钮----------------------------
    def select_cur_list(index):
        global list_select_index_all
        list_select_index_all = index
        refresh_data()

    row_t = row_t + 1
    mbutton0 = Menubutton(frame_t, text=room_list[list_select_index_all].ServerID, relief=RAISED)
    picks0 = Menu(mbutton0)
    mbutton0.config(menu=picks0)
    mbutton0.grid(row=row_t, column=0, columnspan=3, sticky=W + E + N + S)
    for (index, value) in enumerate(room_list):
        picks0.add_command(label=value.ServerID, command=lambda index=index: select_cur_list(index))

    # --------------------------------------------------------------------------------
    # ---------选择房间和机器人的下拉按钮-----------------------------------------------------------------
    # --------------------------------------------------------------------------------
    row_t = row_t + 1
    frame_t = Frame(root)
    frame_t.grid(row=row_t, column=0,  columnspan=1, sticky=W+E+N+S)
    frame_t2 = Frame(root)
    frame_t2.grid(row=row_t, column=2,  columnspan=3, sticky=W+E)

    label1 = Label(frame_t, text="房间的类型...")
    label1.grid(row=row_t, column=0, sticky=W)

    label3 = Label(frame_t2, text="机器人类型...")
    label3.grid(row=row_t, column=3, sticky=W)

    # ------添加menuButton列表---------------------------------------------
    game_room_sql_list = NewGameRoomSql
    android_sql_list = SqlFiles

    # 通过点击事件获取房间类型index---------------------
    def menu_button_fuc1(index):
        global list_select_index1
        list_select_index1 = index
        mbutton1.config(text=game_room_sql_list[int(index)])
        input2.delete(0, END)
        input2.insert(0, get_room_name())  # 房间名字改为生成方式

    mbutton1 = Menubutton(frame_t, text=game_room_sql_list[0], relief=RAISED)
    picks1 = Menu(mbutton1)
    mbutton1.config(menu=picks1)
    mbutton1.grid(row=row_t, column=1, sticky=W+E+N+S)
    for (index, value) in enumerate(game_room_sql_list):
        picks1.add_command(label=value, command=lambda index=index: menu_button_fuc1(index))

    # 通过点击事件获取机器人类型index----------------------------
    def menu_button_fuc2(index):
        global list_select_index2
        list_select_index2 = index
        mbutton2.config(text=android_sql_list[int(index)])

    mbutton2 = Menubutton(frame_t2, text=android_sql_list[0], relief=RAISED)
    picks2 = Menu(mbutton2)
    mbutton2.config(menu=picks2)
    mbutton2.grid(row=row_t, column=4, sticky=W+E+N+S)
    for (index, value) in enumerate(android_sql_list):
        picks2.add_command(label=value, command=lambda index=index: menu_button_fuc2(index))

    # --------------------------------------------------------------------------------
    # -----------------输入4个属性控件------------------------------------------------
    # --------------------------------------------------------------------------------
    row_t = row_t + 1
    frame_t = Frame(root)
    frame_t.grid(row=row_t, column=0,  columnspan=8, sticky=W+E)

    label = Label(frame_t, text="房间ID编号...")
    label.grid(row=row_t, column=0)
    input1 = Spinbox(frame_t, from_=0, to=100000)
    input1.grid(row=row_t, column=1, sticky=W)

    # row_t = row_t + 1
    label = Label(frame_t, text="房间名字...")
    label.grid(row=row_t, column=2)
    input2 = Entry(frame_t)
    input2.grid(row=row_t, column=3,  columnspan=8, sticky=W+E)

    row_t = row_t + 1
    label = Label(frame_t, text="机器人数量...")
    label.grid(row=row_t, column=0)
    input3 = Spinbox(frame_t, from_=0, to=100)
    input3.grid(row=row_t, column=1, sticky=W)

    label = Label(frame_t, text="版本号...")
    label.grid(row=row_t, column=2)
    # input3 = Spinbox(frame_t, from_=0, to=100)
    # input3.grid(row=row_t, column=3, sticky=W)
    # -----------------button list ------------
    verion_sql_list = Versions

    def select_verions(index):
        global list_select_index3
        list_select_index3 = index
        mbutton4.config(text=verion_sql_list[int(index)])
        input2.delete(0, END)
        input2.insert(0, get_room_name())  # 房间名字改为生成方式

    mbutton4 = Menubutton(frame_t, text=verion_sql_list[0], relief=RAISED)
    picks4 = Menu(mbutton4)
    mbutton4.config(menu=picks4)
    mbutton4.grid(row=row_t, column=4, sticky=W+E+N+S)
    for (index, value) in enumerate(verion_sql_list):
        picks4.add_command(label=value, command=lambda index=index: select_verions(index))

    # -----------------------------------------
    row_t = row_t + 1
    label = Label(frame_t, text="机器码...")
    label.grid(row=row_t, column=0)
    input4 = Entry(frame_t)
    input4.grid(row=row_t, column=1, columnspan=4, sticky=W+E)

    # # ---------文件选择框--------------------
    # def file_dialog_open():
    #     my_file_types = [('Python files', '*.py'), ('All files', '*')]
    #     open1 = fd.Open(root, filetypes=my_file_types)
    #     str1 = open1.show()
    #     Message(root, text=str1).grid(row=7, column=0)
    #
    # # ----------------Menu-------------------------------------------
    # menubar = Menu(root)
    # filemenu = Menu(menubar, tearoff=0)
    # filemenu.add_command(label="Open", command=file_dialog_open)
    # filemenu.add_command(label="Save", command=file_dialog_open)
    # filemenu.add_separator()
    # filemenu.add_command(label="Exit", command=root.quit)
    # menubar.add_cascade(label="File", menu=filemenu)
    #
    # # create more pulldown menus
    # editmenu = Menu(menubar, tearoff=0)
    # editmenu.add_command(label="Cut", command=file_dialog_open)
    # editmenu.add_command(label="Copy", command=file_dialog_open)
    # editmenu.add_command(label="Paste", command=file_dialog_open)
    # menubar.add_cascade(label="Edit", menu=editmenu)
    #
    # helpmenu = Menu(menubar, tearoff=0)
    # helpmenu.add_command(label="About", command=file_dialog_open)
    # menubar.add_cascade(label="Help", menu=helpmenu)
    #
    # # display the menu
    # root.config(menu=menubar)

    # ------------------添加button和自定义事件----------------------------------
    def start_open_server():

        mt([r"-r", r"-m", r"-s"])
        # msgbox.showinfo('Message', '恭喜！')
        # Message(root, text=str(input1.get())).grid(row=9, column=0)
        # Message(root, text=str(input2.get())).grid(row=9, column=1)
        # Message(root, text=str(input3.get())).grid(row=9, column=2)
        # Message(root, text=str(input4.get())).grid(row=9, column=3)
        # Message(root, text=str(list_select_index1)).grid(row=9, column=4)
        # Message(root, text=str(list_select_index2)).grid(row=9, column=5)
        # Message(root, text=str(list_select_index_all)).grid(row=9, column=6)

    row_t = row_t + 1
    button = Button(root, text='退出', command=root.quit)
    button.grid(row=row_t, column=6, padx=10, pady=10)
    label = Label(root, text="点击一键开服之后，列表中的所有信息将注入数据库！")
    label.grid(row=row_t, column=0, columnspan=3)
    button = Button(root, text='一键开服', command=start_open_server)
    button.grid(row=row_t, column=3,  padx=10, pady=10)

    row_t = row_t + 1
    label = Label(root, text="Version: 1.04")
    label.grid(row=row_t, column=0, sticky=W)

    # --------------刷新显示数据---------------------
    def refresh_data():
        global list_select_index1
        list_select_index1 = int(room_list[list_select_index_all].GameRoomListIndex)
        mbutton1.config(text=game_room_sql_list[list_select_index1])

        global list_select_index2
        list_select_index2 = int(room_list[list_select_index_all].SqlFileRobotListIndex)
        mbutton2.config(text=android_sql_list[list_select_index2])

        # global list_select_index3
        # list_select_index3 = int(room_list[list_select_index_all].SqlFileRobotListIndex)
        # mbutton2.config(text=android_sql_list[list_select_index2])

        mbutton0.config(text=str(room_list[list_select_index_all].ServerID))

        input1.delete(0,END)
        input2.delete(0,END)
        input3.delete(0,END)
        input4.delete(0,END)
        input1.insert(0, room_list[list_select_index_all].ServerID)
        # input2.insert(0, room_list[list_select_index_all].ServerName)

        input2.insert(0, get_room_name())       # 房间名字改为生成方式
        input3.insert(0, room_list[list_select_index_all].AndroidCount)
        input4.insert(0, room_list[list_select_index_all].ServerMachine)

        list_all.select_clear(0, END)
        list_all.select_set(list_select_index_all)

    # 功能函数，房间名字默认填充
    def get_room_name():
        room_name = NewGameRoomSql[list_select_index1]
        room_name = room_name.split(".")[0]
        return room_name + "[%s]" % room_list[list_select_index_all].ServerID + "_%s" % Versions[list_select_index3]



    # --------------------开始loop---------------------
    refresh_data()
    root.mainloop()


if __name__ == "__main__":
    main()



