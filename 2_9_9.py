import re 
s=input()
po = re.findall(r'\d(?P<second>[a-z]{5})\w\second', s)
#po = re.findall(r'([а-яА-ЯёЁa-zA-Z])\1', s)
#po = re.findall(r'(\d{3})\1', s)
print(po)