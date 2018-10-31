# -*- coding: UTF-8 -*-

# 奔驰宝马


SUB_C_REQ_BANKER = 400  # 申请上庄
SUB_S_REQ_BANKER = 401  # 坐庄
SUB_S_BANKER_REQ_RESULT = 402  # 申请结果
SUB_S_BANKER_SITUSERINFO = 403  # 坐庄信息

SUB_S_ChipStart = 404  # 下注开始
SUB_S_ChipStop = 405  # 下注结束

SUB_C_UserChip = 406  # 玩家下注
SUB_S_ChipSucc = 407  # 下注成功
SUB_S_Control_UserChip = 408  # 玩家下注

SUB_C_ContinueChip = 409  # 玩家续投
SUB_S_ContinueChip = 410  # 续投回应

SUB_S_GameStart = 411  # 游戏开始
SUB_S_GameEnd = 412  # 游戏结束
SUB_S_Game_ResultInfo = 413  # 庄家游戏结算信息

SUB_C_Control_SetDst = 414  # 控制结果
SUB_C_Control_SelectDst = 415  # 选中目标玩家
SUB_S_Control_DealRet = 416  # 处理结果

SUB_C_ClearChip = 417  # 清空投注
SUB_S_ClearChip = 418  # 清空投注回应

SUB_C_UpdateSelfScore = 419  # 更新自己分数
SUB_S_UpdateSelfScore = 420  # 更新自己分数

SUB_S_Sence_Free = 421  # 空闲场景
SUB_S_GameResultInfo = 422  # 普通玩家游戏结算信息
SUB_S_BondLost = 423  # 奖池空了
SUB_S_UpdataChip = 424  # 更新下注
SUB_S_Control_Update = 425  # 控制数据更新
SUB_S_SysMessage = 426  # 系统消息
SUB_S_UpdateUserInfo = 427  # 玩家信息
SUB_S_GameInfo = 428  # 游戏信息
SUB_S_GameOpenLog = 429  # 游戏开奖纪录
SUB_S_SelfResult = 430  # 自己计算信息
SUB_S_BankerResult = 431  # 庄家结果信息
SUB_S_Control_UserInfo = 432  # 玩家信息
SUB_S_Control_StockInfo = 433  # 库存信息
SUB_S_Control_UserLeave = 434  # 玩家离开
SUB_S_UserChipNotify = 435  # 玩家下注数据广播给所有用户
SUB_S_UserContinueChipNotify = 436  # 玩家续投数据广播给所有用户
SUB_S_AndroidUpdataChip = 437  # 通知机器人下注
SUB_S_UserTotalChipNotify = 438  # 通知超级管理员总下注信息

SUB_C_ONLINE_TOTAL = 439  # 请求服务器在线人数
SUB_S_ONLINE_TOTAL = 440  # 服务器返回在线人数
SUB_C_ROBBANKREQUEST = 441  # 客户端请求抢庄
