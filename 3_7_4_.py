import re
pattern = r'https://imgur.com/[a-zA-Z0-9]{7}'
s=input()
it = re.findall(pattern,s)
print(*it,sep="\n")
