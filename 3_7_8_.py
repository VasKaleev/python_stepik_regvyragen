import re
s = input()
#pattern = r'<a.*href="([^"]+)">'
pattern = r'<a.+?href="([^"]+).+?a>'
it = re.findall(pattern,s)
print(*it,sep="\n")
