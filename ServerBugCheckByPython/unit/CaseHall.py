# -*- coding: UTF-8 -*-
import random

from proto.CMD_LoginServer_pb2 import *
from proto.CMD_Common_pb2 import *
from proto.CMD_GlobalServer_pb2 import *
from proto.CMD_GlobalServer_Inner_pb2 import *
from proto.CMD_GameServer_pb2 import *
from const.protocol_ls import *
from const.protocol_gs import *


import Setting
from Send import SendFunc


class PlayActionHall(object):
    def __init__(self):
        self.userid=Setting.UserID

    # 30日签到领奖
    def send_msg_activity_sign_thirty(self):
        cmd = CMD_MB_C_Sign_Thirty()
        cmd.user_id = self.userid  # 用户userid
        cmd.last_day = -1  # 签到的天数
        cmd.is_first_thirty = True  # 是否是三十日
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_ACTIVITY, SUB_MB_C_ACTIVITY_SIGN_THIRTY, s)
        print("30日签到领奖")

    # 轮盘抽奖（话费、金币）
    def send_msg_activity_play_dial_ex(self):
        cmd = CMD_MB_C2S_PlayDial_Ex()
        cmd.user_id = self.userid  # 用户userid
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_ACTIVITY, SUB_MB_C2S_ACTIVITY_PLAY_DIAL_EX, s)
        print("轮盘话费抽奖")

    def send_msg_activity_play_dial_money(self):
        cmd = CMD_MB_C2S_PlayDial_Money()
        cmd.user_id = self.userid  # 用户userid
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_ACTIVITY, SUB_MB_C2S_ACTIVITY_PLAY_DIAL_MONEY, s)
        print("轮盘金币抽奖")

    def send_msg_c2l_reward_get(self):
        cmd = CMD_MB_C2S_ADD_REWARD()
        cmd.user_id = self.userid
        reasonList=[1,2,3,4,5,6,7,8,9,10]
        cmd.client_type = 4
        cmd.channel_id = 11
        cmd.game_id = 8
        cmd.reason_type = reasonList[random.randint(0,len(reasonList)-1)]
        print(cmd.reason_type)
        cmd.extend_infos.append(1)
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_REWARD, SUB_MB_C2L_REWARD_GET, s)
        print("分享获得奖励—鱼池")

    # 礼包码兑换
    def send_msg_c2s_fresh_package_ex(self):
        cmd = CMD_MB_C2S_Fresh_Package_Ex()
        cmd.user_id = self.userid
        cmd.fresh_key = ('123').encode('utf-8')  # 文本转byte 不知道是不是这么写滴
        cmd.channel_id = 11
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_ACTIVITY, SUB_MB_C2S_ACTIVITY_FRESH_PACKAGE_EX, s)
        print("礼包码兑换")

    # 领取好友红包
    def send_msg_accept_invite(self):
        cmd = CMD_MB_C_ACCEPT_INVITE()
        cmd.invite_key = ('123').encode('utf-8')  # 文本转byte 不知道是不是这么写滴
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_ACTIVITY, SUB_MB_C_ACCEPT_INVITE, s)
        print("领取好友红包")

    # 邮件领取奖励
    def send_msg_eamil_get_attachment_c2g(self):
        cmd = CMD_MB_C_Message_GetGift()
        cmd.user_id = self.userid
        cmd.get_index_list.append(1)
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_MESSAGE, SUB_MB_C_MESSAGE_GET_GIFT, s)
        print("领取邮件奖励")

    # 更换头像
    def send_msg_modify_face(self):
        cmd = CMD_MB_ModifyFace()
        cmd.face_id = 1  # 头像ID
        cmd.user_id = self.userid
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO, SUB_MB_MODIFY_FACE, s)
        print("更换头像")

    # 改变昵称
    def send_msg_modify_nickname(self):
        cmd = CMD_MB_ModifyNickName()
        cmd.nick_name = ('-1').encode('utf-8')  # 文本转byte 不知道是不是这么写滴
        cmd.user_id = self.userid
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO, SUB_MB_C_MODIFY_NICKNAME, s)
        print("改变昵称")

    # 获取手机验证码
    def send_msg_register_confirm_code_from_game(self):
        cmd = CMD_MB_RegisterRequestConfirmCode()
        cmd.mobile_phone = ('18108356933').encode('utf-8')  # 文本转byte 不知道是不是这么写滴
        desData = ''
        # string output = string.Format("Action=sms&_time={0}&KindID={1}&mobile={2}", Utility_Function.GetTimeStamp(), CommonVariable.GameId, cellphonenumber);
        # string desData = TemplatePlugins.Utility.UnityEngineHelperFunc.EncryptDES(output, CommonVariable.DESStringKey);
        cmd.post_data = "pack=" + desData
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_BIND, SUB_C2G_GET_PHONE_CONFIRMCODE, s)
        print("获取手机验证码")

    # 手机号绑定
    def send_msg_guest_bingding(self):
        cmd = CMD_MB_GuestBinding()
        cmd.user_id = self.userid
        cmd.mobile_phone = ('18108356933').encode('utf-8')
        cmd.confirm_code = ('123455').encode('utf-8')  # 验证码
        cmd.machine_id = "180F1ABFA5010B0CFDCAC41BE48DB3CA"
        cmd.is_email_binding = 1  # 0 或1
        desData = ''
        # string output = string.Format("Action=sms&_time={0}&KindID={1}&mobile={2}", Utility_Function.GetTimeStamp(), CommonVariable.GameId, cellphonenumber);
        # string desData = TemplatePlugins.Utility.UnityEngineHelperFunc.EncryptDES(output, CommonVariable.DESStringKey);
        cmd.post_data = "pack=" + desData
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_LOGON, SUB_MB_GUESTBINGDING, s)
        print("绑定手机号")

    # 手机号解绑 CL_REMOVE_BIND 发送解除绑定验证码协议

    # 首次赠送密码  CLS_CMD_SET_GIVE_PASSWORD 首次设置赠送密码协议

    # 修改赠送密码 CLS_CMD_MODIFY_GIVE_PASSWORD_G2C 修改赠送密码协议

    # 赠送道具
    def send_msg_give_nick(self):
        cmd = CMD_MB_C_GIVE_NICKNAME()
        cmd.user_id = self.userid
        cmd.give_game_id = 2020202  # 填写要赠送的玩家游戏ID
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO, SUB_MB_C_GIVE_NICKNAME, s)
        print("赠送道具—请求对方ID")

    def send_msg_give_away_item(self):
        cmd = CMD_MB_C_GIVE_ITEM()
        cmd.user_id = self.userid
        cmd.item_id = 110
        cmd.item_number =4200000100
        cmd.give_game_id = 20202020  # 填写要赠送的玩家游戏ID
        passwordStr = ""
        # C#里面有转换操作 具体使用时候打断点看
        cmd.give_password = (passwordStr).encode('utf-8')
        print("赠送道具")

    # 钻石购买道具
    def send_msg_buy_item(self):
        cmd = CMD_MB_C_BUY_ITEM()
        cmd.user_id = self.userid
        cmd.item_id = 110
        cmd.item_number =4200000100
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO, SUB_MB_C_BUY_ITEM, s)
        print("钻石购买道具")

    # 分解道具
    def send_msg_break_item(self):
        cmd = CMD_MB_C_BREAK_ITEM()
        cmd.break_count = 1
        cmd.item_id = 4200000100
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO, SUB_MB_C_BREAK_ITEM, s)
        print("分解道具")

    # 使用道具
    def send_msg_sell_item(self):
        cmd = CMD_MB_C_SELL_ITEM()
        cmd.user_id = self.userid
        cmd.item_id = 1
        cmd.item_number =4200000100
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO, SUB_MB_C_SELL_ITEM, s)
        print("使用道具")

    # 合成道具
    def send_msg_compound_item(self):
        cmd = CMD_MB_C_COMPOUND_ITEM()
        cmd.compound_count = 1
        cmd.item_id = 4200000100
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO, SUB_MB_C_COMPOUND_ITEM, s)
        print("合成道具")

    #活跃度领奖
    def send_msg_get_liveness_reward(self):
        cmd=CMD_MB_C_GET_LIVENESS_REWARD()
        cmd.reward_id=-1
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_MISSION,SUB_MB_C_GET_LIVENESS_REWARD,s)
        print("活跃度领奖")

    #每日任务 #本周任务 #成长任务
    def send_msg_get_mission_reward(self):
        cmd=CMD_MB_C_GET_MISSION_REWARD()
        cmd.mission_id=1 #任务ID
        cmd.mission_type=1 #任务类型
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_MISSION,SUB_MB_C_GET_MISSION_REWARD,s)
        print("每日任务")

    #锻造
    def send_msg_levelup_site(self):
        cmd=CMD_MB_C_LEVELUP_SITE()
        cmd.iLevelId=1
        cmd.isUseItem=True #哪个啥 直接成功滴？
        #cmd.siteType= 2
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_LEVELUP_SITE,s)
        print("锻造")

    #请求在线奖励
    def send_msg_get_online_gift_check_get(self):
        cmd=CMD_C_GET_ONLINE_GIFT_CHECK_GET()
        cmd.user_id=self.userid
        cmd.nType=-1
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_ONLINE_GIFT_REQ,s)
        print("请求在线奖励")

    #请求在线奖励列表
    def send_msg_get_online_gift_type(self):
        cmd=CMD_C_GET_ONLINE_GIFT_TYPE()
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_ONLINE_GIFT_TYPE_REQ,s)
        print("请求在线奖励列表")

    #请求更新我的礼包
    def send_msg_my_gift_pack(self):
        cmd=CMD_C_MY_GIFT_PACK
        cmd.user_id=self.userid
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_GIFT_PACK,SUB_MB_C2L_MY_GIFT_PACK_INFO,s)
        print("请求更新我的礼包")

    #领取7日礼包请求  前端没有代码了
    def send_msg_seven_day_gift_get(self):
        cmd=CMD_C_SEVEN_DAY_GIFT_GET()
        cmd.user_id=self.userid
        cmd.gift_id=-1
        cmd.version=200000
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_USER,SUB_GR_C_SEVEN_DAY_GIFT_GET,s)

    #、、、
    def send_msg__GetDialMoneyInfo(self):
        cmd=CMD_MB_C2S_GetDialMoneyInfo()
        cmd.user_id=self.userid
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_ACTIVITY,SUB_MB_C2S_ACTIVITY_PLAY_DIALMONEY,s)
        print("无名协议")


    #得到奖励（绑定，首冲）
    def send_msg_get_reward(self):
        cmd=CMD_MB_C2S_Get_Reward()
        cmd.user_id=self.userid
        cmd.type=random.randint(1,2)
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_ACTIVITY,SUB_MB_C2S_GET_REWARD,s)
        print("得到奖励（绑定，首冲）")

    #、、、
    def send_msg_product_info(self):
        cmd=CMD_MB_C2L_PRODUCT_INFO()
        cmd.user_id=self.userid
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_PURCHASE,SUB_MB_C2L_PRODUCT_INFO,s)
        print("无名协议")

    #请求刷新金币奖券
    def send_msg_RefreshMoney(self):
        cmd=CMD_MB_C_RefreshMoney()
        cmd.user_id=self.userid
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_REFRESH_MONEY,s)
        print("请求刷新金币奖券")

    #砖石兑换金币
    def send_msg_diamond_exchange(self):
        cmd=CMD_MB_C2S_DIAMOND_EXCHANGE()
        cmd.user_id=self.userid
        cmd.diamond=20
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_PURCHASE,SUB_MB_C2S_DIAMOND_EXCHANGE,s)  #大厅
        #SendFunc(MDM_MB_PURCHASE, SUB_GR_C2S_DIAMOND_EXCHANGE, s) #游戏服
        print("砖石兑换金币")

    #、、、
    def send_msg_dial_record(self):
        cmd=CMD_C_DIAL_RECORD()
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_DIAL_RECORD,s)
        print ("无名协议")

    #请求竞技场排名
    def send_msg_request_arena_rank(self):
        cmd=CMD_MB_C_REQUEST_ARENA_RANK()
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_REQUEST_ARENA_RANK,s)
        print ("请求竞技场排名")

    #解锁炮
    def send_msg_unlock_cannon_multiple(self):
        cmd=CMD_MB_C_UNLOCK_CANNON_MULTIPLE()
        cmd.level=4200000020
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_UNLOCK_CANNON_MULTIPLE,s)
        print("解锁炮")


    #领取邀请奖励
    def send_msg_get_invite_reward(self):
        cmd=CMD_MB_C_GET_INVITE_REWARD()
        cmd.gift_id=1
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_ACTIVITY,SUB_MB_C_GET_INVITE_REWARD,s)
        print("领取邀请奖励")

    #获取时间礼包
    def send_msg_get_timegift(self):
        cmd=CMD_MB_C_GET_TIMEGIFT()
        cmd.timegift_id=3
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_GET_TIMEGIFT,s)
        print("获取时间礼包")

    #点赞
    def send_msg_click_praise(self):
        cmd=CMD_MB_C_CLICK_PRAISE()
        cmd.user_id=self.userid
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_CLICK_PRAISE,s)
        print("点赞")

    #领取解锁炮倍数奖励
    def send_msg_unlock_cannon_reward(self):
        cmd=CMD_MB_C_GET_UNLOCK_CANNON_REWARD()
        cmd.day=3
        cmd.select_reward=3
        cmd.real_name=('zht').encode('utf-8')
        cmd.mobile_phone=('18108356933').encode('utf-8')
        cmd.id_num=('111').encode('utf-8')
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_GET_UNLOCK_CANNON_REWARD,s)
        print("领取解锁炮倍数奖励")

    # 转换道具
    def send_msg_rechange_item(self):
        cmd=CMD_MB_C_RECHANGE_ITEM()
        itemList=[101,107,110,120,130,150,1001,2001,2005,6001,7001,10001,10005,10014,10023,10026]
        cmd.item_id=itemList[random.randint(0,len(itemList)-1)]
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_RECHANGE_ITEM,s)
        print("转换道具")
        print (cmd.item_id)

    # H5微端登录领取微端奖励
    def send_msg_get_h5_cltnet_award(self):
        cmd=CMD_C_GET_H5_CLINET_AWARD()
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_GET_H5_CLIENT_AWARD,s)
        print("H5微端登录领取微端奖励")

    # 获取vip锻造优惠
    def send_msg_vipForge(self):
        cmd=CMD_C_vipForge()
        cmd.viplv=1
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_MB_C_VIP_FORGE,s)
        print("获取vip锻造优惠")


    # 领取vip房间每日任务奖励
    def send_msg_get_vip_room_mission_reward(self):
        cmd=CMD_C_GET_VIP_ROOM_MISSION_REWARD()
        cmd.cell_score=4200000100
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO,SUB_C_GET_VIP_ROOM_MISSION_REWARD,s)
        print("领取vip房间每日任务奖励")

    #轮盘中奖人信息
    # def send_msg_LuckyGuyInfo(self):
    #     cmd=LuckyGuyInfo()
    #     cmd.user_id=self.userid
    #     cmd.nick=1
    #     cmd.reward=1
    #     cmd.face_id=1
    #     cmd.vip_lev=1
    #     s = cmd.SerializeToString()
    #     SendFunc()

    #获取奖池信息
    def send_msg_get_classic_prize_pool(self):
        cmd=CMD_C_GET_CLASSIC_PRIZE_POOL()
        cmd.type=1
        cmd.pool_type=1
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME,SUB_C_CLASSIC_PRIZE_POOL_STOCK,s)
        print("获取奖池信息")

    MAIN_FANTASY_EXHIBITION = 1004
    SUB_SC_DROP_LOTTERY=2

    #梦幻展览 用户请求掉落展品
    def send_msg_fantasy_drop_lottery(self):
        cmd=CMD_C_FANTASY_DROP_LOTTERY()
        cmd.userId=self.userid
        cmd.contribute=100
        cmd.multiple=28
        cmd.jointimes=1
        cmd.ipaytotal=100
        cmd.viplev=1
        cmd.faceid=1
        cmd.nick=('zht').encode('utf-8')
        cmd.costpool=1
        s = cmd.SerializeToString()
        SendFunc(1004,2,s)
    print("梦幻展览 用户请求掉落展品")

    # #领取周常藏宝阁奖励
    # def send_msg_get_week_reward(self):
    #     cmd=CMD_MB_C_GET_WEEK_REWARD()
    #     cmd.puzzles_id=-1
    #     s = cmd.SerializeToString()
    #     SendFunc()


CaseHall=PlayActionHall()