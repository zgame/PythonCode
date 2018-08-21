# coding=utf-8
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.filedialog as fd


list_select_index_all = 0
list_select_index1 = 0
list_select_index2 = 0

def main():

    row_t = 0

    root = Tk()

    # --------title-----------------------------
    root.title("Tools")
    # -------添加label---------------------------------------------------------
    label = Label(root, text="双击！双击！选择对应的数据...", font=("微软雅黑", 12))
    label.grid(row=row_t, column=1)

    row_t = 1

    # -------添加listBox---------------------------------------------------------
    def printcurList(event):
        global list_select_index_all
        list_select_index_all = list_all.curselection()[0]
        print(list_select_index_all)


    list_a = ['2072', 'room2072', 'port', '23232323223', '50', '1', '8']
    list_all = Listbox(root, height=25, width=25, selectmode=SINGLE, listvariable=StringVar(value=list_a))
    list_all.bind('<Double-Button-1>', printcurList)
    list_all.select_set(0)
    list_all.grid(row=row_t, column=1, columnspan=4, sticky=W+E+N+S)

    # --------滚动条-----------------------
    sl = Scrollbar(root)
    sl.config(command=list_all.yview)
    sl.grid(row=row_t, column=5, sticky=W + S + N)
    list_all.config(yscrollcommand=sl.set)

    # ---------添加2个label-----------------------------------------------------------------
    row_t = 2
    label1 = Label(root, text="房间的类型...")
    label1.grid(row=row_t, column=1)
    label2 = Label(root, text="")
    label2.grid(row=row_t, column=2)
    label3 = Label(root, text="机器人类型...")
    label3.grid(row=row_t, column=3)

    # ------添加menuButton列表---------------------------------------------
    row_t = 3
    li = ['C', 'python', 'php', 'html', 'SQL', 'java', 'python', 'php', 'html', 'SQL', 'java', 'python', 'php', 'html',
          'SQL', 'java', 'python', 'php', 'html', 'SQL', 'java', 'python', 'php', 'html', 'SQL', 'java', 'python',
          'php', 'html', 'SQL', 'java']
    movie = ['CSS', 'jQuery', 'Bootstrap']

    def menu_button_fuc1(index):
        global list_select_index1
        list_select_index1 = index
        mbutton1.config(text=li[int(index)])

    mbutton1 = Menubutton(root, text=li[0], relief=RAISED)
    picks1 = Menu(mbutton1)
    mbutton1.config(menu=picks1)
    mbutton1.grid(row=row_t, column=1)
    for (index, value) in enumerate(li):
        picks1.add_command(label=value, command=lambda index=index: menu_button_fuc1(index))

    def menu_button_fuc2(index):
        global list_select_index2
        list_select_index2 = index
        mbutton2.config(text=movie[int(index)])

    mbutton2 = Menubutton(root, text=movie[0], relief=RAISED)
    picks2 = Menu(mbutton2)
    mbutton2.config(menu=picks2)
    mbutton2.grid(row=row_t, column=3)
    for (index, value) in enumerate(movie):
        picks2.add_command(label=value, command=lambda index=index: menu_button_fuc2(index))

    # -----------------input------------------------------------------------
    row_t = 5
    label = Label(root, text="房间ID编号...")
    label.grid(row=row_t, column=0)
    input1 = Spinbox(root, from_=0, to=100000)
    input1.grid(row=row_t, column=1)

    label = Label(root, text="房间名字...")
    label.grid(row=row_t, column=2)
    input2 = Entry(root)
    input2.grid(row=row_t, column=3)

    row_t = 6
    label = Label(root, text="机器人数量...")
    label.grid(row=row_t, column=0)
    input3 = Spinbox(root, from_=0, to=100, values=(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
    input3.grid(row=row_t, column=1)

    label = Label(root, text="机器码...")
    label.grid(row=row_t, column=2)
    input4 = Entry(root)
    input4.grid(row=row_t, column=3)

    # ---------文件选择框--------------------
    def fileDialogOpen():
        my_file_types = [('Python files', '*.py'), ('All files', '*')]
        open1 = fd.Open(root, filetypes=my_file_types)
        str1 = open1.show()
        Message(root, text=str1).grid(row=7, column=0)

    # ----------------Menu-------------------------------------------
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=fileDialogOpen)
    filemenu.add_command(label="Save", command=fileDialogOpen)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=fileDialogOpen)
    editmenu.add_command(label="Copy", command=fileDialogOpen)
    editmenu.add_command(label="Paste", command=fileDialogOpen)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=fileDialogOpen)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    root.config(menu=menubar)

    # ------------------添加button和自定义事件----------------------------------

    def show_msg():
        msgbox.showinfo('Message', '恭喜！')
        Message(root, text=str(input1.get())).grid(row=9, column=0)
        Message(root, text=str(input2.get())).grid(row=9, column=1)
        Message(root, text=str(input3.get())).grid(row=9, column=2)
        Message(root, text=str(input4.get())).grid(row=9, column=3)
        Message(root, text=str(list_select_index1)).grid(row=9, column=4)
        Message(root, text=str(list_select_index2)).grid(row=9, column=5)
        Message(root, text=str(list_select_index_all)).grid(row=9, column=6)

    row_t = 7
    button = Button(root, text='Quit', command=show_msg)
    button.grid(row=row_t, column=6, padx=10, pady=10)
    # --------------------开始loop---------------------
    root.mainloop()


if __name__ == "__main__":
    main()
