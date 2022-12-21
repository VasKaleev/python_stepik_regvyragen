import re 
s=input()
po = re.findall(r'(?<!\w)(?:0\.[\d]{1,2})(?!\w)|(?<![.\d])[01](?![.\d])',s)
print(po)