import re 
s=input()
po = re.findall(r'(?P<test>\d{3})(?P=test)', s)
#po = re.findall(r'([a-z]{4})', s)
#po = re.findall(r'(\d{3})\1', s)
print(po)