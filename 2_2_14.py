import re 
s = input()
po = re.findall("[A-F0-9]", s)
print(po)