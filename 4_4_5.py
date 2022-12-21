import re
s=input()
res1 = re.sub(r'(\d{2})(\W)(\d{2})\2(\d{4})',r'\3\2\1\2\4',s)
print(res1)