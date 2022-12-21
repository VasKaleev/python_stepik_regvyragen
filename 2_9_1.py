import re 
s=input()
#po = re.findall(r'(?P<test>\d{3})(?P=test)', s)
po = re.findall(r'\d{2}\d{2}', s)
print(po)