# -*- coding: UTF-8 -*-

from Application import *
from unit.DemoCaseFqzs import *
from unit.DemoCaseDfmj import  *
from unit.DemoCaseXsjc import  *



import sys
reload(sys)
sys.setdefaultencoding('utf8')


def run_case(name):
    if name == "楚汉争霸":
        G_App.run_case(unit_chzb)
        G_App.start()
    elif name=="竞猜合集":
        G_App.run_case(unit_xsjc)
        G_App.start()



    """
    if name == "捕鱼":
        G_App.run_case(DemoCase())
        G_App.start()

    elif name == "捕鱼2":
        G_App.run_case_ex(DemoCase())
        G_App.start_ex()
        G_App.wait()
    """




def main():

    run_case("竞猜合集")
    print "app over"



if __name__ == '__main__':
    main()
