import re
pattern = r'[\d]{2},[\d]{4} ₽'
s=input()
it = re.finditer(pattern,s)
for i in it:
    print(i.group())
