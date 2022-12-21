import re 
s=input()
#po = re.findall(r'\b[:][8][;][¦][=]+\b', s)
po = re.findall(r'[а-яёА-ЯЁa-zA-Z].*?[а-яёА-ЯЁa-zA-Z]', s)
print(po)