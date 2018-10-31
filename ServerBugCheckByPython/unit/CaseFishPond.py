# -*- coding: UTF-8 -*-
import random

from proto.CMD_LoginServer_pb2 import *
from proto.CMD_Common_pb2 import *
from proto.CMD_Game_pb2 import *
from proto.CMD_GlobalServer_pb2 import *
from const.protocol_ls import *
from const.protocol_gs import *
import Setting
from Send import SendFunc

class PlayActionFinsPond(object):
    def __init__(self):
        self.userid=Setting.UserID

    #解锁炮倍
    def send_msg_unlock_cannon_multiple(self):
        cmd=CMD_C_UNLOCK_CANNON_MULTIPLE()
        cmd.level=31 #解锁炮倍等级
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME, SUB_C_UNLOCK_CANNON_MULTIPLE, s)
        print("解锁炮倍")

    #购买技能
    def send_msg_buy_skill(self):
        cmd=CMD_C_BUY_SKILL()
        cmd.skill_id=110
        cmd.count=-1
        cmd.target_id=1
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME,SUB_C_BUY_SKILL,s)
        print("购买技能")

    #获取救济金
    def send_msg_get_alms(self):
        cmd=CMD_C_GET_ALMS()
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME,SUB_C_GET_ALMS,s)
        print("领取救济金")

    #猜大小
    def send_msg_num_val(self):
        cmd=CMD_C_NUM_VAL()
        cmd.my_result=-1
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME,SUB_C_NUM_VAL,s)
        print("猜大小")

    #点击获取红包
    def send_msg_red_envelope(self):
        cmd=CMD_C_GET_RED_ENVELOPE()
        cmd.user_id=self.userid
        cmd.envelope_id=4200000100
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME,SUB_C_GET_RED_ENVELOPE,s)
        print("点击获取红包")

    #BOSS轮盘请求
    def send_msg_boss_roulette_req(self):
        cmd=CMD_C_BOSS_ROULETTE_REQ()
        cmd.bet_money=1
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME,SUB_C_BOSS_ROULETTE_REQ,s)
        print("Boss轮盘请求")


    #触发随机倍数请求
    def send_msg_random_multple_req(self):
        cmd=CMD_C_RANDOM_MULTIPLE_REQ()
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME,SUB_C_RANDOM_MULTIPLE_REQ,s)
        print("触发随机倍数请求")

    #幸运猜大小
    def send_msg_classic_prize_pllo_guess(self):
        cmd=CMD_C_CLASSIC_PRIZE_POOL_GUESS()
        typeList = [0,1,2]
        cmd.type=typeList[random.randint(0,len(typeList)-1)]
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME,SUB_C_CLASSIC_PRIZE_POOL_GUESS,s)
        print("幸运猜大小")

    #领取幸运猜大小奖金
    def send_msg_classic_prize_pool_guesss_get(self):
        cmd=CMD_C_CLASSIC_PRIZE_POOL_GUESS_GET()
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME,SUB_C_CLASSIC_PRIZE_POOL_GUESS_GET,s)
        print("领取幸运猜大小奖金")

    #领取活动奖励
    def send_msg_get_lucky_number_reward(self):
        cmd=CMD_C_GET_LUCKY_NUMBER_REWARD()
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_USER,SUB_GR_C_GET_LUCKY_NUMBER_REWARD,s)
        print("领取活动奖励")

    # 通过幸运数字任务充值
    def send_msg_recharge_in_lucky_number(self):
        cmd=CMD_C_RECHARGE_IN_LUCKY_NUMBER()
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_USER,SUB_MB_C_LUCKY_NUMBER_RECHARGE,s)
        print("通过幸运数字任务充值")

    #领取新手连续登陆奖励
    def send_msg_user_loginday_reward(self):
        cmd=CMD_C_USER_LOGINDAY_REWARD()
        cmd.user_id=self.userid
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_USER,SUB_MB_C_USER_LOGINDAY_REWARD,s)
        print("领取新手连续登陆奖励")

    #领取狂欢福利活动信息
    def send_msg_carnival_welfare_info(self):
        cmd=CMD_C_CARNIVAL_WELFARE_INFO()
        cmd.user_id=self.userid
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_USER,SUB_GR_C_CARNIVAL_WELFARE_INFO,s)
        print("领取狂欢福利活动信息")


    #抽取狂欢福利活动数字
    def send_msg__CARNIVAL_WELFARE_DRAW(self):
        cmd=CMD_C_CARNIVAL_WELFARE_DRAW()
        cmd.user_id=self.userid
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_USER,SUB_MB_C_DRAW_CARNIVAL_WELFARE,s)
        print("抽取狂欢福利活动数字")


    #领取狂欢福利活动奖励
    def send_msg_CARNIVAL_WELFARE_REWARD(self):
        cmd=CMD_C_CARNIVAL_WELFARE_REWARD()
        cmd.user_id=self.userid
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_USER,SUB_MB_C_CARNIVAL_WELFARE_REWARD,s)
        print("领取狂欢福利活动奖励")

    # 使用子弹皮肤（跟换子弹皮肤）
    def send_msg_ExchangeBulletSkid(self):
        cmd = CMD_MB_C_BUY_BULLET_SKIN()
        cmd.buy_skin_id = 1
        s = cmd.SerializeToString()
        SendFunc(MDM_MB_USER_INFO, SUB_MB_C_BUY_BULLET_SKIN, s)
        print("跟换子弹皮肤")

    # 分享获得奖励(登录服、鱼池分享)
    def send_msg_c2g_reward_get(self):
        cmd = CMD_MB_C2S_ADD_REWARD()
        cmd.user_id = self.userid
        cmd.client_type = 4
        cmd.channel_id = 11
        cmd.game_id = 8
        cmd.reason_type = 3
        cmd.extend_infos.append(1)
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_REWARD, SUB_C2G_REWARD_GET, s)
        print("分享获得奖励—登录服")

    #奖池轮盘抽奖
    def send_msg_classic_prize_pool_draw_turn(self):
        cmd=CMD_C_CLASSIC_PRIZE_POOL_DRAW_TURN()
        cmd.star=1
        cmd.player.user_id =self.userid
        cmd.player.nick=('zht').encode('utf-8')
        cmd.player.reward=1
        cmd.player.face_id=1
        cmd.player.vip_lev=1
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME,SUB_C_CLASSIC_PRIZE_POOL_GUESS,s)
        print("奖池轮盘抽奖")

    # 奖池轮盘抽奖排行
    def send_msg_classic_prize_pool_turn_rank(self):
        cmd = CMD_C_CLASSIC_PRIZE_POOL_TURN_RANK()
        s = cmd.SerializeToString()
        SendFunc(MDM_GF_GAME, SUB_C_CLASSIC_PRIZE_POOL_RANK, s)
        print("奖池轮盘抽奖排行")

    #、、、
    def send_msg_purchase_trade_view_status(self):

        cmd=CMD_MB_C2S_PURCHASE_TRADE_VIEW_STATUS()
        cmd.user_id=self.userid
        cmd.local_language=('1').encode('utf-8')
        cmd.recharge_type=1
        cmd.recharge_value=1
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_PURCHASE,SUB_C2G_PURCHASE_TRADE_VIEW_STATUS,s)
        print("无名协议")

    #领取任务奖励
    def send_msg_get_lucky_number_task_reward(self):

        cmd=CMD_C_GET_LUCKY_NUMBER_TASK_REWARD()
        cmd.task_id=7004
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_USER,SUB_GR_C_GET_LUCKY_NUMBER_TASK_REWARD,s)
        print("领取任务奖励")

    #客户端请求领取奖励
    def send_msg_mission_bereward(self):
        cmd=CMD_C_Mission_BeReward()
        cmd.mission_id=1
        s = cmd.SerializeToString()
        SendFunc(MDM_GR_NEWMISSION,SUB_GR_C_MISSION_BEWARD,s)
        print("客户端请求领取奖励")

    #发射子弹
    def send_msg_user_fire(self):
        cmd=CMD_C_USER_FIRE()
        cmd.tick_count=0
        cmd.angle=130
        cmd.lock_fish_id=0
        cmd.bullet_mulriple=1
        cmd.bullet_temp_id=0
        cmd.bullet_num=1
        cmd.is_broadcast=True
        cmd.is_double=False
        cmd.sf_skill_id=0
        cmd.monster_upper=1
        s = cmd.SerializeToString()
        SendFunc(7,116,s)
        print("发射子弹")

    #碰撞鱼
    def send_msg_catch_fish(self):
        cmd=CMD_C_CATCH_FISH()
        cmd.fish_uid=1
        cmd.bullet_id=1
        cmd.bullet_temp_id=2
        cmd.chair_id=1
        cmd.weakness_id=1
        s = cmd.SerializeToString()
        SendFunc(7,113,s)
        print("碰撞魚")



CaseFishPond=PlayActionFinsPond()
