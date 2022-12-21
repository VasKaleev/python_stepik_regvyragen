import re
#pattern = r'(^[1-9]{1}$|^[1-4]{1}[0-9]{1}$|^50$)'
#pattern = r'(\+7)+'
#pattern = r'(^\+7|7|8)+'
#pattern = r'\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b'
pattern = r'^((8|\+7|7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,11}$'
s=input()
s2 = re.fullmatch(pattern,s)
print(s2)
if s2 is not None:
    print("True")
else:
    print("False")