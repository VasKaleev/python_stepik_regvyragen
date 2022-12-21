import re 
s=input()
po = re.findall(r'(\b\w+)-?\1\b',s)
print(po)