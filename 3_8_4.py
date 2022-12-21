import re 
s=input()
po = re.split(r'(?:Категория: [А-Яа-я ]+\\n|\\n)', s)
a=[]
for i in po:
    if i!="":
        a.append(i)
print(*a,sep="\n")