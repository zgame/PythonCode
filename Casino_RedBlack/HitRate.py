import random
# 循环100万次， 看5次随机猜红黑之后， 总体收益率是赔还是赚

# 多次猜红黑， 猜的次数越多越容易输， 偶尔赢能赢大的
print("---------------------------red black hit rate--------------------------")


# 随机  [a, b]
def get_random(a, b):
    return random.randint(a, b)


# 翻牌
def get_card():
    gold = 1
    for _ in range(5):
        red_black = get_random(0, 1)  # 翻牌
        select_card = get_random(0, 1)  # 选牌
        if red_black == select_card:
            gold = gold * 2
            # print("翻牌 %s   选牌 %s   gold: %s" % (red_black, select_card, gold))
        else:
            gold = 0
            # print("翻牌 %s   选牌 %s   gold: 0     失败" % (red_black, select_card))
            break
    return gold


sum1 = 0
# 循环
for i in range(1000000):
    if i%10000 == 0:
        print("%d%%--------------------------" % (i/10000))
    sum1 = sum1 + get_card()

print("----------------------------------------------------------------   ", sum1)
