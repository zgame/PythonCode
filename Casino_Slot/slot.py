# -------------------------------------------------------------------
#   老虎机
# -------------------------------------------------------------------
import random
import time
import slot_lines_50

# -----------------------------牌类型----------------------------------
# 类型定义
card_type = ["W", "A", "K", "Q", "J", "9", "8", "7"]
card_type_wild = "W"

# -----------------------------倍率表----------------------------------
win_multi = [
    [0, 0, 0],
    [50, 100, 200],
    [50, 100, 200],
    [50, 100, 200],
    [50, 100, 200],
    [5, 10, 20],
    [5, 10, 20],
    [5, 10, 20],
]


# 生成随机阵
def generate_matrix():
    my_matrix = []
    for i in range(slot_lines_50.LineHeight * slot_lines_50.LineWidth):
        my_matrix.append(random.randint(0, len(card_type) - 1))
    return my_matrix


# 打印矩阵
def print_matrix(my_matrix):
    # print(my_matrix)
    for i in range(slot_lines_50.LineHeight):
        line = ""
        for j in range(slot_lines_50.LineWidth):
            line = line + " " + card_type[my_matrix[i * slot_lines_50.LineWidth + j]]
        print(line)
    print("-------------------matrix-------------")


# 计算单一行是否满足3个原则
def calculate_one_line(my_line):
    result = 0
    # 如果前2个一样， 或者其中有一个是万能，符合
    if my_line[0] == my_line[1] or my_line[0] == card_type_wild or my_line[1] == card_type_wild:
        # print("前2个ok")
        # 如果第3个跟前2个任何一个一样，或者第3个是万能，符合
        if my_line[2] == my_line[1] or my_line[2] == my_line[0] or my_line[2] == card_type_wild:
            # print("前3个ok，三联")
            result = 3
            # 如果第4个跟前3个任何一个一样，或者第4个是万能，符合
            if my_line[3] == my_line[2] or my_line[3] == my_line[1] or my_line[3] == my_line[0] or \
                    my_line[3] == card_type_wild:
                # print("前4个ok， 四联")
                result = 4
                # 如果第5个跟前4个任何一个一样，或者第5个是万能，符合
                if my_line[4] == my_line[3] or my_line[4] == my_line[2] or my_line[4] == my_line[1] or \
                        my_line[4] == my_line[0] or my_line[4] == card_type_wild:
                    # print("前5个ok， 五联")
                    result = 5
    return result


# 遍历所有线进行查找
def run_lines_all(my_matrix):
    # 遍历50条线
    for line in slot_lines_50.win_line:
        matrix_line = []
        # 组合成用来判断的连线
        for i in range(len(line)):
            matrix_line.append(card_type[my_matrix[line[i] * slot_lines_50.LineWidth + i]])
        # print(matrix_line)
        # 对连线进行判断
        result = calculate_one_line(matrix_line)
        if result > 0:
            print(result, "连线")


# -----------------------------Run----------------------------------

# slot_lines_50.print_all_lines()     # 测试用打印线路
matrix = generate_matrix()
print_matrix(matrix)
now = time.time()
# print("time.time(): %f " % now)
run_lines_all(matrix)  # 遍历所有线查找
print("time cost: %f 毫秒" % ((time.time() - now) * 1000))
# print("time.time(): %f " % time.time())

# print_matrix(generate_matrix())
