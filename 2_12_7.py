import re 
s=input()
po = re.findall(r'(\b[А-Яа-яЁё]*а[А-Яа-яЁё]*)(?![0-9_]\b)',s)
print(po)