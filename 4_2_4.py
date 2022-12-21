import re
s=input()
res = re.findall(r'(\d{3})(\1+)', s)
for i in res:
    print(*i,sep="", end=" ")