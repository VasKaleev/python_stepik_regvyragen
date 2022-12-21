import re 
s=input()
po = re.findall(r'\w*[а-яА-ЯЁё]+[^а-яА-ЯЁё\s]+\w*\b|\w*[^а-яА-ЯЁё\s]+[а-яА-ЯЁё]+\w*\b',s)
print(po)