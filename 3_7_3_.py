import re
pattern = r'[\d]{11}'
s=input()
it = re.findall(pattern,s)
print(*it,sep="\n")
