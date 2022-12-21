import re 
s=input()
#po = re.findall(r'(?P<test>\d{3})(?P=test)', s)
po = re.findall(r'([а-яА-ЯёЁa-zA-Z])\1', s)
#po = re.findall(r'(\d{3})\1', s)
print(po)