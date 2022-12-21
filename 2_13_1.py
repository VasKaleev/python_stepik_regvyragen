import re 
s=input()
po = re.findall(r'(?<=[^\.]\s)[a-z]+[a-zA-Z0-9][^\W_]+(?=\b)',s)
print(po)