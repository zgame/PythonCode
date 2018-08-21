# -*- coding: UTF-8 -*-


## 网络通信协议
####################################################################
## 主协议
COMMON = 1
## 游戏协议
GAME = 2
## 心跳
KEEPLIVE = 12



## 登录子协议
COMMON_SUB_C_LOGIN = 1  ##请求登录
COMMON_SUB_S_LOGIN = 2  ##登录回复
COMMON_SUB_S_COINCHG = 3 ## 元宝变更

COMMON_SUB_S_KICK = 11   ## 踢下线
COMMON_SUB_C_LEAVE = 12  ## 玩家主动离开
COMMON_SUB_S_LEAVE = 13

COMMON_SUB_S_ACTIVITY_INFO = 14 ## 活动信息
COMMON_SUB_S_PLAYER_ACTIVITY_INFO = 15 ## 玩家活动信息
COMMON_SUB_C_PLAYER_GET_ACTIVITY_AWARD = 16 ## 玩家获取活动奖励
COMMON_SUB_S_PLAYER_GET_ACTIVITY_AWARD = 17 ## 玩家获取活动奖励返回
COMMON_SUB_S_ACTIVITY_RULES_INFO = 18 ## 活动规则部分数据

COMMON_SUB_S_ROLL_MSG = 20  ## 本服跑马灯信息


## 游戏子协议
####################################################################
GAME_SUB_S_SITDOWN = 1
GAME_SUB_S_STATE_CHG = 2        ## 游戏状态变更
GAME_SUB_S_DRAW = 3             ## 开奖
GAME_SUB_C_CHIP = 4             ## 下注
GAME_SUB_S_CHIP = 5             ## 下注
GAME_SUB_C_CHIP_EX = 6          ## 下注
GAME_SUB_S_CHIP_EX = 7          ## 下注
GAME_SUB_S_CHIP_INFO = 8        ## 下注信息
GAME_SUB_S_USER_TRAD = 9        ## 玩家开奖结算
GAME_SUB_S_TABLE_USER_COUNT = 10## 当前桌子在线人数
GAME_SUB_C_SWITCH_MODE = 11      ## 切换游戏模式
GAME_SUB_S_SWITCH_MODE = 12      ## 切换游戏模式
GAME_SUB_C_GAMECONFIG = 13      ## 游戏配置
GAME_SUB_S_GAMECONFIG = 14      ## 游戏配置

GAME_SUB_C_RANK                 = 15           ##客户端请求分数排行          ###>cmd_c_game_rank
GAME_SUB_S_RANK                 = 16           ##服务器请求分数排行          ###>cmd_s_game_rank

GAME_SUB_C_GET_REWARD           = 17           ##客户端发过来领取奖励      ####>cmd_c_game_get_reward
GAME_SUB_S_GET_REWARD           = 18           ##服务器发过去领取奖励      ####>cmd_s_game_get_reward


## 游戏子协议 金蝉捕鱼
####################################################################
GAME_SUB_S_ROOM_LIST            = 101           ##发送房间列表给客户端
GAME_SUB_C_SELECT_ROOM          = 102           ##选择房间
GAME_SUB_S_SELECT_ROOM          = 103           ##返回选择房间信息，失败的时候才返回，成功的直接返回进入场景的消息
GAME_SUB_S_ENTER_SCENE          = 104			##进入场景
GAME_SUB_C_EXIT_SCENE           = 105           ##退出场景，退到选择房间界面
GAME_SUB_S_EXIT_SCENE           = 106           ##退出场景，退到选择房间界面
GAME_SUB_S_OTHER_ENTER_SCENE    = 107			##其他人进入场景
GAME_SUB_S_SCENE_FISH           = 108		    ##场景鱼
GAME_SUB_S_DISTRIBUTE_FISH      = 109			##服务器生成鱼
GAME_SUB_C_USER_FIRE            = 110			##客户端开火
GAME_SUB_S_USER_FIRE            = 111			##服务器返回开火
GAME_SUB_C_CATCH_FISH           = 112			##捕获鱼儿
GAME_SUB_S_CATCH_FISH           = 113			##服务器返回捕获鱼儿
GAME_SUB_C_CHANGE_BULLET        = 114			##改变子弹倍率
GAME_SUB_S_CHANGE_BULLET        = 115			##服务器返回改变子弹倍率
GAME_SUB_S_SWITCH_SCENE         = 116			##转换场景
GAME_SUB_S_BOSS_COME            = 117           ##BOSS来了消息
GAME_SUB_S_UPDATE_SCORE         = 118           ##通知玩家更新元宝

## 游戏子协议 三国武道会
####################################################################
GAME_SUB_S_SPECIAL_AREA_INFO    = 200
GAME_SUB_C_SPECIAL_AREA_INFO    = 201

## 游戏子协议 挖矿传奇 从5000开始
####################################################################
GAME_SUB_C_DIG                  = 5000           ##客户端发过来挖矿消息
GAME_SUB_S_DIG                  = 5001           ##服务器返回挖矿消息
GAME_SUB_SITDOWN                = 5002           ##服务器发给客户端进入房间坐下消息
GAME_SUB_C_BAT                  = 5003           ##客户端发给服务前的赌石
GAME_SUB_S_BAT                  = 5004           ##服务器发给客户端的赌石结果
GAME_SUB_C_OPEN_BAT             = 5005           ##客户端发给服务前的开启赌石
GAME_SUB_S_OPEN_BAT             = 5006          ##服务器发给客户端的开启赌石
GAME_SUB_S_UPATE_JACKPOT        = 5007          ##通知客户端更新奖励池
GAME_SUB_S_UPATE_FCOIN          = 5008          ##通知客户端更新元宝
GAME_SUB_C_BOX_REWARD_RECORD    = 5009           ##客户端请求宝箱奖励纪录
GAME_SUB_S_BOX_REWARD_RECORD    = 5010           ##服务器返回宝箱奖励纪录

## 游戏子协议 青蛙跳一跳 从 5020开始
####################################################################
GAME_SUB_C_START                = 5020           ##客户端发过来的开始跳一跳协议
GAME_SUB_S_START                = 5021           ##服务器返回开始跳一跳协议
GAME_SUB_C_JUMP                 = 5022           ##客户端发过来每一次跳跃的结果
GAME_SUB_S_JUMP                 = 5023           ##服务器返回每一次跳跃的结果
GAME_SUB_C_RELIFE               = 5024           ##客户端发过来的复活协议
GAME_SUB_S_RELIFE               = 5025           ##服务器返回复活协议
GAME_SUB_C_END                  = 5026           ##客户端发过来结算游戏
GAME_SUB_S_END                  = 5027           ##服务器返回结算游戏
GAME_SUB_QWTYT_SITDOWN          = 5028           ##服务器发给客户端进入房间坐下消息

## 游戏子协议 2048 从 5030开始
####################################################################
GAME_SUB_C_START_2048           = 5030           ##客户端发过来的开始2048协议####>cmd_c_game_start
GAME_SUB_S_START_2048           = 5031           ##服务器返回开始2048协议    #####>cmd_s_game_start
GAME_SUB_C_MOVE                 = 5032           ##客户端发过来每一次移动滑块 #####>cmd_c_game_move
GAME_SUB_S_MOVE                 = 5033           ##服务器返回每一次移动的结果 ######>cmd_s_game_move
GAME_SUB_C_RELIFE               = 5034           ## 客户端发过来的复活消息       ####>cmd_c_game_relife
GAME_SUB_S_RELIFE               = 5035           ## 服务器返回的复活消息       ####>cmd_s_game_relife

GAME_SUB_2048_SITDOWN           = 5038           ##服务器发给客户端进入房间坐下消息 ###>cmd_game_sitdown


## 游戏子协议 猜拳 从 6000开始
####################################################################

GAME_SUB_CQ_SITDOWN           = 6000           ##服务器发给客户端进入房间坐下消息 ###>cmd_game_sitdown
GAME_SUB_C_START_CQ           = 6001           ##客户端发过来的开始猜拳比赛协议####>cmd_c_game_start
GAME_SUB_S_START_CQ           = 6002           ##服务器返回开始协议    #####>cmd_s_game_start
GAME_SUB_S_NOTIFY_CQ          = 6003           ##服务器奖池返回金币同步协议    #####>cmd_s_jackpot_notify
GAME_SUB_C_WINNING_CQ         = 6004           ##客户端获取奖池中奖记录协议    #####>cmd_c_game_winning
GAME_SUB_S_WINNING_CQ         = 6005           ##服务器返回开始协议    #####>cmd_c_game_winning
GAME_SUB_C_CQ_TYPE            = 6006           ##客户端选择猜拳类型协议    #####>cmd_c_game_cq_type
GAME_SUB_S_CQ_TYPE            = 6007           ##服务器返回选择猜拳类型协议    #####>cmd_s_game_cq_type

## 现实竞猜的子协议 从6000开始
####################################################################
##GAME_XSJC_S_SITDOWN                   = 6000;
##GAME_XSJC_S_GUESSITEM                = 6001;
GAME_XSJC_C_SELECT_ITEM              = 6002;
GAME_XSJC_S_WIN_PRIZE                   = 6003;
GAME_XSJC_S_AGENDA_LIST             = 6004;
GAME_XSJC_S_WORLDCUP_LIST        = 6005;
GAME_XSJC_S_REALITY_LIST               = 6006;
GAME_XSJC_S_REALITY_DATA            = 6007                      ## 更新现实竞猜某一题 的数据
GAME_XSJC_C_AGENDA_UPDATE      = 6008;
GAME_XSJC_S_AGENDA_UPDATE       = 6009;
GAME_XSJC_C_MATCH_UPDATE        = 6010;
GAME_XSJC_S_MATCH_UPDATE        = 6011;                     ## 更新某项比赛 的数据
GAME_XSJC_C_RECORD_LIST            = 6012;
GAME_XSJC_S_RECORD_LIST            = 6013;
GAME_XSJC_C_RECORD_DETAIL       = 6014;
GAME_XSJC_S_RECORD_DETAIL        = 6015;
GAME_XSJC_C_WORLDCUP            = 6016
GAME_XSJC_S_WORLDCUP            = 6017
GAME_XSJC_C_WORLDCUP_RESULT     = 6018
GAME_XSJC_S_WORLDCUP_RESULT     = 6019
GAME_XSJC_S_UPDATE_JACKPOT = 6020
GAME_XSJC_C_REQUEST_CHIP_RANK_INFO = 6021
GAME_XSJC_S_REQUEST_CHIP_RANK_INFO = 6022
GAME_XSJC_S_REQUEST_CHIP_RANK_AWARD_INFO = 6023

## 数据库指令
####################################################################
## 1~100 为大厅, 公共指令
DB_CMD_LOAD_GAME_CFG = 1                                ## 加载游戏配置项
DB_CMD_LOAD_GAME_DATA = 2                               ## 加载游戏数据
DB_CMD_LOAD_USERGAME_DATA = 3                           ## 加载用户游戏数据
DB_CMD_GAME_AUTH = 4                                    ## 游戏登录
DB_CMD_LOAD_DAY_MAXWINLOSE = 5                          ## 加载当日最大输赢
DB_CMD_LOAD_GAME_RANK_DATA = 6                          ## 加载游戏排行榜数据
DB_CMD_LOAD_GAME_RANK_AWARD_DATA = 7                    ## 加载游戏排行榜数据
DB_CMD_LOAD_GAME_RANK_CONFIG = 8                        ## 加载游戏排行榜配置数据
DB_CMD_LOAD_GAME_SPECIAL_LOG_DATA = 9                   ## 加载游戏特殊记录数据
DB_CMD_LOAD_PLYAER_SPECIAL_LOG_DATA = 10                ## 加载玩家特殊记录数据
DB_CMD_LOAD_GAME_SERVER_INFO = 11                       ## 加载服务器信息
DB_CMD_LOAD_GAME_ACTIVITY_DATA = 12                     ## 加载游戏活动相关配置数据
DB_CMD_LOAD_GAME_ACTIVITY_PROGRESS_DATA = 13            ## 加载游戏活动进度配置表
DB_CMD_LOAD_GAME_ACTIVITY_AWARD_DATA = 14               ## 加载游戏活动奖励配置表
DB_CMD_LOAD_UPDATE_GAME_ACTIVITY_DATA = 15              ## 加载游戏活动相关配置数据（后台通知更新）
DB_CMD_LOAD_UPDATE_GAME_ACTIVITY_PROGRESS_DATA = 16     ## 加载游戏活动进度配置表
DB_CMD_LOAD_UPDATE_GAME_ACTIVITY_AWARD_DATA = 17        ## 加载游戏活动奖励配置表
DB_CMD_LOAD_UPDATE_GAME_ACTIVITY_SPECIAL_AWARD_DATA = 18## 加载游戏活动特殊奖励奖励配置表

DB_CMD_LOAD_GAME_SPECIAL_RANK_DATA_1 = 19               ## (特殊排行榜) {加载球王争夺赛排名数据,竞猜投注排行榜}
DB_CMD_LOAD_GAME_SPECIAL_RANK_DATA_2 = 20              ## (特殊排行榜) {加载历届排行榜数据}
DB_CMD_LOAD_JACKPORT_RANK = 21                                  ## 奖池获奖名单1
DB_CMD_LOAD_JACKPORT2_RANK = 22                                 ## 奖池获奖名单2

## 数据库指令 金蝉捕鱼
####################################################################
DB_CMD_LOAD_USER_DATA = 101                     ## 加载玩家游戏数据
DB_CMD_LOAD_USER_ACTIVITY_DATA = 102            ## 加载玩家游戏活动数据

## 现实竞猜 数据库操作
DB_CMD_XSJC_GUESS_ITEMS = 106                           ## 获取竞猜类别
DB_CMD_XSJC_MATCH_LIST = 107                                ## 获取比赛列表
DB_CMD_XSJC_MATCH_OPTIONS = 108                     ##获取足球比赛选项
DB_CMD_XSJC_WORLDCUP_LIST = 109                     ## 获取世界杯投注列表
DB_CMD_XSJC_WORLDCUP_OPTIONS = 110             ## 获取世界杯的选项
DB_CMD_XSJC_REALITY_LIST = 111                          ##获取 现实竞猜列表
DB_CMD_XSJC_REALITY_OPTIONS = 112                   ## 获取现实竞猜选项
DB_CMD_XSJC_ADD_MATCH = 113                         ## 添加新的足球比赛
DB_CMD_XSJC_UPATE_MATCH = 114                       ## 更新比赛信息
DB_CMD_XSJC_PRIZE_LAMP = 115                            ## 开奖时的跑马灯提示

DB_CMD_XSJC_WORLDCUP_RANK = 116              ## 世界杯4，8强玩家排名
DB_CMD_XSJC_FINAL4_STATISTICS = 117                 ## 世界杯4强 统计
DB_CMD_XSJC_FINAL4_AND_DRAW  = 118              ## 4强开奖时查询 总人数 和 总下注额
DB_CMD_XSJC_ORDER_LIST = 119                ## 玩家的订单列表

DB_CMD_XSJC_ORDER_MAXID = 120                         ## 获取足球订单表，最大ID值

DB_CMD_XSJC_BALL_ORDER_DATA = 123               ## 加载玩家现实竞猜球类订单
DB_CMD_XSJC_REALL_OREDE_DATE = 124              ## 加载玩家显示竞猜现实玩法订单
DB_CMD_XSJC_WORLDCU_ORDER_DATE = 125            ## 加载玩家现实竞猜世界杯玩法订单

## HTTP请求指令
## 玩家相关
####################################################################
HTTP_CMD_AUTH = 1           ##登录认证
HTTP_CMD_EXCHANGE = 2       ##兑换查询
HTTP_CMD_CHANGE_COIN = 3    ## 元宝变更
HTTP_CMD_KEEPLIVE = 4       ## 平台心跳

## 平台相关
####################################################################
HTTP_CMD_BASE = 1000

## 游戏子协议 射门 #############################################

GAME_SUB_C_PLAY_BALL = 13              ##开始踢球
GAME_SUB_S_PLAY_BALL = 14              ##响应开始踢球
GAME_SUB_C_SELECT_CHIP = 15            ##选择筹码
GAME_SUB_S_SELECT_CHIP = 16             ##响应选择筹码
GAME_SUB_S_JACKPOT_NOTIFY = 17         ##奖池金币同步
GAME_SUB_C_RANK_DATA = 18             ##获取球王争霸排行
GAME_SUB_S_KING_RANK_DATA = 19         ##响应球王数据
GAME_SUB_C_GET_AWARD_RECORD = 20             ##获取奖池记录
GAME_SUB_S_GET_AWARD_RECORD = 21         ##响应奖池记录
GAME_SUB_C_LEAVE_ROOM = 22                      ## 玩家离开房间



