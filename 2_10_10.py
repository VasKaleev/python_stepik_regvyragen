import re 
s=input()
po = re.findall(r'(?<=[^\.]\s)[A-ZА-ЯЁ][^\W0-9_]+(?=\b)', s)
#po = re.findall(r'([а-яА-ЯёЁa-zA-Z])\1', s)
#po = re.findall(r'(\d{3})\1', s)
print(po)