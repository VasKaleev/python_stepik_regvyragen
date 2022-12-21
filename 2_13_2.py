import re 
s=input()
po = re.findall(r'\b[a-z0-9_]+\b',s)
print(po)