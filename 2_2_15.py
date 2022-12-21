import re 
s = input()
po = re.findall("[1-9][1-9][1-9] кабинет", s)
print(po)