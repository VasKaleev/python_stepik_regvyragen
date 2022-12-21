import re
pattern = '(?:[78]|\+7)(?:[\s\-()]*\d){10}'
s=input()
s2 = re.fullmatch(pattern,s)
print(s2)
if s2 is not None:
    print("True")
else:
    print("False")