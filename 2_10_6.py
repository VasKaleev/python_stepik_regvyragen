import re 
s=input()
po = re.findall(r'\b\d*[02468]\b', s)
#po = re.findall(r'([а-яА-ЯёЁa-zA-Z])\1', s)
#po = re.findall(r'(\d{3})\1', s)
print(po)