# -*- coding: UTF-8 -*-


# 网络通信协议
# --------------------------------------------------------------------
# 主协议
COMMON = 1
GAME = 2

# 登录子协议
COMMON_SUB_C_LOGIN = 1  # 请求登录
COMMON_SUB_S_LOGIN = 2  # 登录回复
COMMON_SUB_S_COINCHG = 3  # 元宝变更

COMMON_SUB_S_KICK = 11      # 踢下线
COMMON_SUB_C_LEAVE = 12     # 玩家主动离开
COMMON_SUB_S_LEAVE = 13

COMMON_SUB_S_ROLL_MSG = 20  # 本服跑马灯信息


# 游戏子协议
# --------------------------------------------------------------------
GAME_SUB_S_SITDOWN = 1          # 坐下
GAME_SUB_S_STATE_CHG = 2        # 游戏状态变更
GAME_SUB_S_DRAW = 3             # 开奖
GAME_SUB_C_CHIP = 4             # 下注
GAME_SUB_S_CHIP = 5
GAME_SUB_C_CHIP_EX = 6          # 下注
GAME_SUB_S_CHIP_EX = 7          # 下注
GAME_SUB_S_CHIP_INFO = 8        # 下注信息
GAME_SUB_S_USER_TRAD = 9        # 玩家开奖结算