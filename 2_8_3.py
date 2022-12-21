import re 
s=input()
#po = re.findall(r'\b[:][8][;][¦][=]+\b', s)
po = re.findall(r'\d{0,}?1', s)
print(po)