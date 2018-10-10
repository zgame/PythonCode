# -*- coding: UTF-8 -*-

from Application import *
from unit.DemoCase import *
from unit.DemoCaseBSMC import *
from unit.DemoCaseBSMC2 import *
from unit.DemoCaseChat import *
from unit.DemoCaseSGJ import *
from unit.DemoCaseSGJ2 import *
from unit.DemoCaseSHZ import *
from unit.DemoCaseSHZ2 import *

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def run_case(name):
    if name == "宝石迷城":      # 设定开奖几率,统计分数分布
        G_App.run_case(DemoCaseBSMC())
        G_App.start()
    if name == "宝石迷城2":     # 给定金额,杀分赞助值,统计分数变化情况
        G_App.run_case(g_case_bsmc2)
        G_App.start()
    elif name == "水浒传":
        G_App.run_case(DemoCaseSHZ())
        G_App.start()
    elif name == "水浒传2":    # 给定金额,杀分赞助值,统计分数变化情况
        G_App.run_case(g_case_shz2)
        G_App.start()
    elif name == "水果机":
        G_App.run_case(DemoCaseSGJ())
        G_App.start()
    elif name == "水果机2":   # 给定金额,杀分赞助值,统计分数变化情况
        G_App.run_case(g_case_sgj2)
        G_App.start()
    elif name == "聊天系统":
        G_App.run_case(g_case_chat)
        G_App.start()
    elif name == "捕鱼":
        G_App.run_case(DemoCase())
        G_App.start()
    elif name == "捕鱼2":
        G_App.run_case_ex(DemoCase())
        G_App.start_ex()
        G_App.wait()


def main():
    run_case("捕鱼")
    print("app over")


if __name__ == '__main__':
    main()
