import re 
s=input()
#po = re.findall(r'\b[:][8][;][¦][=]+\b', s)
#po = re.findall(r"Привет, Олег|Привет, Григорий|Пока, Олег|Пока, Григорий", s)
po = re.findall(r".+", s)
# :^P ¦^D :-C :-/ 8-) =-\ 8-C =-0 :-| ¦-O
print(po)