# coding=utf-8
import re
str = "34_67"

re = re.sub(r"\w_",r"._55",str)

re = str.split("_")

print re