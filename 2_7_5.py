import re 
s=input()
#s='р258мв097 р369оа04 а932ву004'
#авекмнорстух
po = re.findall(r'regex =r"[авекмнорстух]\d{3}[авекмнорстух]{2}[^0]\d*', s)
#po = re.findall(r'[авекмнорстух][0-9]\d\d[авекмнорстух][авекмнорстух][1-9][0-9][0-9]{,3}|[авекмнорстух][0-9]\d\d[авекмнорстух][авекмнорстух][1-9]', s)
print(po)