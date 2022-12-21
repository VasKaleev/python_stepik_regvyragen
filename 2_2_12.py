import re 
s = input()
po = re.findall("[Пп]ривет", s)
print(po)