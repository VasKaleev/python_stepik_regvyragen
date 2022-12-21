import re 
s = input()
po = re.findall("со[нкм]", s)
print(po)