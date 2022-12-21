import re 
s = input()
po = re.findall("[\d]+", s)
print(po)