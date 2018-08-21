# coding=utf-8

# -------------------------------------------------------------------------------

# 更新机器码， 在更新完成之后， 会自动改写SettingMachinecode.py文件，
# 自动把newcode的值填写到oldCode里面，因为上次的老oldCode已经替换掉了，现在newCode跟oldCode一样了
# Author: Zhushw

# -------------------------------------------------------------------------------

from Scripts.MsSql import ODBC_MS
from Setting.SettingDataBase import SqlServerSetting
from Setting.SettingMachineCode import machine_code_list

def main():
    # 遍历所有列表内容
    for i in machine_code_list:
        # 如果机器码不一样， 就更新到数据库
        if i.NewCode != i.OldCode:
            changeCode(i.OldCode, i.NewCode)
            alterFile('SettingMachineCode.py',i.OldCode, i.NewCode)


def alterFile(file, old_str, new_str):
    file_data = ""
    with open(file, 'r') as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line

    file_data = unicode(file_data, "utf-8")
    # print file_data
    with open(file, "w") as f:
        f.write(file_data.encode("utf-8"))


    with open(file, 'r') as f:
        re = f.read()
    print(re)


def changeCode(OldCode, NewCode):
    ms = ODBC_MS('{SQL SERVER}', SqlServerSetting.SERVER_ADRESS, SqlServerSetting.DATABASE, SqlServerSetting.UID,   SqlServerSetting.PWD)
    sql = """
    set nocount on
    DECLARE @updateRowCount int
    UPDATE dbo.GameRoomInfo set ServiceMachine = '%s' where ServiceMachine = '%s'
    select @@ROWCOUNT
    """ % (OldCode, NewCode)
    sql = unicode(sql, "utf-8")
    # print(sql)
    re = ms.ExecQueryExp(sql)
    print("更新了"+ str(re[0][0])+"行!")
    print("GameRoomInfo的机器码已经更新！")




if __name__ == '__main__':
    main()



