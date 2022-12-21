import re 
s=input()
po = re.findall(r'v=([a-zA-Z0-9]+)',s)
print(po)