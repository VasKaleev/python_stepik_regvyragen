import re
s='''
I like flags
I like flags
I like flags
'''
test2 = re.findall(r"\b([a-zA-Z]+)\b", s, flags=re.MULTILINE)
print(test2)  