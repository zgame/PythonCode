# -----------------------------中奖线路----------------------------------
win_line = [
    [0, 0, 0, 0, 0],  # 第一条线
    [1, 1, 1, 1, 1],  #
    [2, 2, 2, 2, 2],  #
    [0, 1, 2, 2, 2],  #
    [2, 1, 0, 0, 0],  #

    [1, 1, 2, 1, 1],  # 6
    [1, 1, 0, 1, 1],  #
    [0, 1, 0, 1, 0],  #
    [1, 2, 1, 2, 1],  #
    [2, 1, 2, 1, 2],  #

    [1, 0, 1, 0, 1],  # 11
    [2, 1, 0, 1, 2],  #
    [0, 1, 2, 1, 0],  #
    [0, 1, 1, 1, 0],  #
    [1, 2, 2, 2, 1],  #

    [2, 1, 1, 1, 2],  # 16
    [1, 0, 0, 0, 1],  #
    [0, 1, 1, 1, 1],  #
    [2, 1, 1, 1, 1],  #
    [1, 0, 1, 2, 1],  #

    [1, 2, 1, 0, 1],  # 21
    [0, 0, 1, 2, 2],  #
    [2, 2, 1, 0, 0],  #
    [0, 0, 2, 0, 0],  #
    [2, 2, 0, 2, 2],  #

    [0, 2, 2, 2, 0],  # 26
    [2, 0, 0, 0, 2],  #
    [1, 2, 0, 2, 1],  #
    [1, 0, 2, 0, 1],  #
    [0, 2, 0, 2, 0],  #

    [2, 0, 2, 0, 2],  # 31
    [2, 0, 1, 2, 0],
    [0, 2, 1, 0, 2],
    [0, 2, 1, 2, 0],
    [2, 0, 1, 0, 2],

    [2, 1, 0, 0, 1],  # 36
    [0, 1, 2, 2, 1],
    [0, 0, 2, 2, 2],
    [2, 2, 0, 0, 0],
    [1, 0, 2, 1, 2],

    [1, 2, 0, 1, 0],  # 41
    [0, 1, 0, 1, 2],
    [2, 1, 2, 1, 0],
    [1, 2, 2, 0, 0],
    [0, 0, 1, 1, 2],

    [2, 2, 1, 1, 0],  # 46
    [2, 0, 0, 0, 0],
    [0, 2, 2, 2, 2],
    [2, 2, 2, 2, 0],
    [0, 0, 0, 0, 2],  # 第五十条线
]

# ----------------------------- 常量定义 ----------------------------------
LineWidth = 5  # 宽
LineHeight = 3  # 高


# ----------------------------- DEBUG ----------------------------------
# 绘制出连线
def print_line(i):
    for j in range(LineHeight):
        show_line = ""
        for k in range(LineWidth):
            if win_line[i][k] == j:
                show_line += " ■"
            else:
                show_line += " □"
        print(show_line)
    print("-----------------------------------", i + 1)


# 绘制出所有连线
def print_all_lines():
    for i in range(len(win_line)):
        print_line(i)
