# -*- coding: UTF-8 -*-


# 飞禽走兽 导弹场


SUB_C_REQ_BANKER = 900  # 申请上庄
SUB_S_REQ_BANKER = 901  # 坐庄
SUB_S_BANKER_REQ_RESULT = 902  # 申请结果
SUB_S_BANKER_SITUSERINFO = 903  # 坐庄信息

SUB_S_ChipStart = 904  # 下注开始
SUB_S_ChipStop = 905  # 下注结束

SUB_C_UserChip = 906  # 玩家下注
SUB_S_ChipSucc = 907  # 下注成功
SUB_S_Control_UserChip = 908  # 玩家下注

SUB_C_ContinueChip = 909  # 玩家续投
SUB_S_ContinueChip = 910  # 续投回应

SUB_S_GameStart = 911  # 游戏开始
SUB_S_GameEnd = 912  # 游戏结束
SUB_S_Game_ResultInfo = 913  # 庄家游戏结算信息

SUB_C_Control_SetDst = 914  # 控制结果
SUB_C_Control_SelectDst = 915  # 选中目标玩家
SUB_S_Control_DealRet = 916  # 处理结果

SUB_C_ClearChip = 917  # 清空投注
SUB_S_ClearChip = 918  # 清空投注回应

SUB_C_UpdateSelfScore = 919  # 更新自己分数
SUB_S_UpdateSelfScore = 920  # 更新自己分数

SUB_S_Sence_Free = 921  # 空闲场景
SUB_S_GameResultInfo = 922  # 普通玩家游戏结算信息
SUB_S_BondLost = 923  # 奖池空了
SUB_S_UpdataChip = 924  # 更新下注
SUB_S_Control_Update = 925  # 控制数据更新
SUB_S_SysMessage = 926  # 系统消息
SUB_S_UpdateUserInfo = 927  # 玩家信息
SUB_S_GameInfo = 928  # 游戏信息
SUB_S_GameOpenLog = 929  # 游戏开奖纪录
SUB_S_SelfResult = 930  # 自己计算信息
SUB_S_BankerResult = 931  # 庄家结果信息
SUB_S_Control_UserInfo = 932  # 玩家信息
SUB_S_Control_StockInfo = 933  # 库存信息
SUB_S_Control_UserLeave = 934  # 玩家离开
SUB_S_UserChipNotify = 935  # 玩家下注数据广播给所有用户
SUB_S_UserContinueChipNotify = 936  # 玩家续投数据广播给所有用户
SUB_S_AndroidUpdataChip = 937  # 通知机器人下注
SUB_S_UserTotalChipNotify = 938  # 通知超级管理员总下注信息

SUB_C_ONLINE_TOTAL = 939  # 请求服务器在线人数
SUB_S_ONLINE_TOTAL = 940  # 服务器返回在线人数
SUB_C_ROBBANKREQUEST = 941  # 客户端请求抢庄
