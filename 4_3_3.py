import re
s=input()
res1 = re.split(r'[A-Za-zА-Яа-яЁё\s\.]+', s)
print(res1)