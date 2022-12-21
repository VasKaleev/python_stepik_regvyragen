import re
s=input()
res = re.findall(r'([0-9]+):([a-z0-9A-Z_]+):([a-z0-9A-Z_]+)', s)
print(res) 