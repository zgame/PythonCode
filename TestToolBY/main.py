# -*- coding: UTF-8 -*-

from Application import *
from unit.DemoCaseFqzs import *
from unit.DemoCaseDfmj import *
from unit.DemoCaseXsjc import *
from unit.DemoCaseJcby import *
from unit.DemoCaseBrnn import *
from unit.DemoCaseMsdmx import *



import sys
reload(sys)
sys.setdefaultencoding('utf8')


def run_case(name):
    if name == "楚汉争霸":
        G_App.run_case(unit_chzb) #登录流程
        G_App.start() #业务逻辑
    elif name=="竞猜合集":
        G_App.run_case(unit_xsjc)
        G_App.start()
    elif name == "大发明家":
        G_App.run_case(unit_dfmj)
        G_App.start()
    elif name=="金蟾捕鱼":
        G_App.run_case(unit_jcby)
        G_App.start()
    elif name=="百人牛牛":
        G_App.run_case(brnn_fqzs)
        G_App.start()
    elif name=="美食大冒险":
        G_App.run_case(unit_msdmx)
        G_App.start()


def main():

    run_case("楚汉争霸")
    print "app over"



if __name__ == '__main__':
    main()
