import re
s = input()
pattern = r'(?:[0-1]\d|2[0-3]):[0-5][0-9]'
it = re.findall(pattern,s)
print(*it,sep="\n")
