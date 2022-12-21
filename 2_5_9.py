import re 
s = input()
po = re.findall("[a-zA-Z0-9_]", s)
print(po)