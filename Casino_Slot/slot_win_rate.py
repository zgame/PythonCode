# -----------------------------中奖几率----------------------------------


# 这里修改用户的整体中奖几率， 可以根据水位增减中奖几率，
def win_rate_change():
    # 根据总体水位，对中奖率的影响
    # 根据个人水位，对中奖率的影响
    # 根据充值情况，对中奖率的影响
    return 1


# 策划控制中奖类型和几率表
win_rate_list = [1,  # 中一条线3连几率
                 1,  # 中一条线4连几率
                 1,  # 中一条线5连几率
                 1,  # 中两条线3连几率
                 1,  # 中两条线4连几率
                 1,  # 中两条线5连几率
                 ]