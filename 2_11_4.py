import re 
s=input()
#po = re.findall(r'\b[:][8][;][¦][=]+\b', s)
po = re.findall(r"\b(?:1|3|bc1)[^ _0OIl\WА-Яа-яёЁ]{27,34}\b", s)
# :^P ¦^D :-C :-/ 8-) =-\ 8-C =-0 :-| ¦-O
print(po)