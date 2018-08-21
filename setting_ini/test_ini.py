import iniparser

conf = iniparser.INIParser()
conf.read('Setting.ini')           

print(conf)
name = conf.get("author")
print(name)
Database = conf.get_section("author")
print(Database.get("ServerIP"))
