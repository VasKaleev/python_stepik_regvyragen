import re 
s = input()
#po = re.findall("^....", s)
po = re.findall("....$", s)
print(po)