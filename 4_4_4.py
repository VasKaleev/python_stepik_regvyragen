import re
s=input()
res1 = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>',s)
res2 = re.sub(r'\*(.*)\*', r'<em>\1</em>',res1)
print(res2)