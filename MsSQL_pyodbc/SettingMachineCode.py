# coding=utf-8

# -------------------------------------------------------------------------------

# 配置机器码
# Author: Zhushw

# -------------------------------------------------------------------------------
# from RunMachineCode import MachineCode

class MachineCode:
    def __init__(self, ServerID, OldCode, NewCode):
        self.ServerID = ServerID
        self.OldCode = OldCode
        self.NewCode = NewCode

    # 用物理机名字查找code
    @staticmethod
    def getMachineCode(ServerID):
        for i in machine_code_list:
            if i.ServerID == ServerID:
                return i.NewCode



machine_code_list = [
    #           物理机             老的机器码                           新的机器码
    MachineCode('GS01', "3109F3ACAEC1EB0ECE96F4EAC311DEE1", "3109F3ACAEC1EB0ECE96F4EAC311DEE1"),
    MachineCode('GS02', "B59CAF259656568644F8D5FE712873D7", "B59CAF259656568644F8D5FE712873D7"),
    MachineCode('GS03', "98A0397115B1FD14C555857AEC7AA454", "98A0397115B1FD14C555857AEC7AA454"),
    MachineCode('GS04', "D0B6A598731E9165EC0CAD74B4902378", "D0B6A598731E9165EC0CAD74B4902378"),
    MachineCode('GS05', "00F2BB341B101788FA38D8725220FF19", "00F2BB341B101788FA38D8725220FF19"),

]
