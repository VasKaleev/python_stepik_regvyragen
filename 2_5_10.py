import re 
s = input()
po = re.findall("[^-1-9^]", s)
print(po)