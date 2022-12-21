import re
pattern = r'\b\w{5}\b'
s=input()
it = re.finditer(pattern,s)
for i in it:
    print(i.group())
