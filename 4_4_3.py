import re
s=input()
res1 = re.sub(r'([а-яА-ЯёЁ]+)\s+\1',r'\1', s)
print(res1)