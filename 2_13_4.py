import re 
s=input()
po = re.findall(r'\b\w*(\.[a-z0-9]*)\b',s)
print(po)