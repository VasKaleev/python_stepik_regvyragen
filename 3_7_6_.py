import re
pattern = r'[0-9]{2}[\.][0-9]{2}[\.][0-9]{4}|[0-9]{4}[\.][0-9]{2}[\.][0-9]{2}|[0-9]{2}[/][0-9]{2}[/][0-9]{4}|[0-9]{4}[/][0-9]{2}[/][0-9]{2}'
s=input()
it = re.findall(pattern,s)
print(*it,sep="\n")
