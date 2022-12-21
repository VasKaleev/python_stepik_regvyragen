import re 
s = input()
po = re.findall("[^a-z_]", s)
print(po)