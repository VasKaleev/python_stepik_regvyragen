import re
#pattern = r'\b[a-z_0-9-]{3,}@[a-z]{3,}.ru|\b[a-z_0-9-]{3,}@[a-z]{3,}.com'
pattern = r'(\b[a-z_0-9-]{3,}@[a-z]{3,}(?:.com|.ru))'
s=input()
it = re.findall(pattern,s)
print(*it,sep="\n")
