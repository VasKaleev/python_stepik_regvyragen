import re 
s=input()
#po = re.findall(r'(?<=[^\.]\s)[a-z0-9_]{5,32}[^-⇒@>*()$!]+(?=\s)',s)
po = re.findall(r'\s([a-z0-9_]{5,32}[^-⇒@>*()$!])\s',s)
print(po)