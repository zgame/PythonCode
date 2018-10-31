# -*- coding: UTF-8 -*-

# 欢乐拼十


SUB_S_GameInfo = 500  # 游戏信息
SUB_S_SysMessage = 501  # 系统消息
SUB_S_SendTableUser = 502  # 上桌玩家信息
SUB_S_UserChipNotify = 503  # 下注通知
SUB_S_GameResultInfo = 504  # 游戏结算信息
SUB_S_RequestBankerList = 505  # 申请庄家列表(进入房间时发送)
SUB_S_RequestBanker = 506  # 申请庄家(单人申请庄家时发送)
SUB_S_UpdateBanker = 507  # 更新庄家信息(每回合结束都会更新)
SUB_S_HistoryRecord = 508  # 发送历史记录
SUB_S_ContiueChip = 509  # 玩家续投结果
SUB_S_UpdateChip = 510  # 上一秒的投注总和
SUB_S_CancelChip = 511  # 取消投注
SUB_S_GOLD_OVER = 512  # 库存被赢光
SUB_C_UserChip = 513  # 玩家下注
SUB_C_RequestBanker = 514  # 申请庄家
SUB_C_ContinueChip = 515  # 玩家续投
SUB_C_CancelChip = 516  # 取消投注
SUB_C_Card_Config = 517  # 配牌操作
SUB_Screen_Control = 518  # 筛选控制
SUB_User_Control = 519  # 用户控制
SUB_Area_Control = 520  # 区域控制
SUB_Get_UserDownInfo = 521  # 获取玩家下注情况
SUB_Send_Game_Info = 522  # 游戏信息
SUB_User_Stand_Up = 523  # 玩家离开
SUB_C_ONLINE_TOTAL = 524  # 请求服务器在线人数
SUB_S_ONLINE_TOTAL = 525  # 服务器返回在线人数
SUB_C_ROBBANKREQUEST = 526  # 客户端请求抢庄
SUB_S_AndroidUpdataChip = 527  # 通知机器人下注
