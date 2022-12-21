import re 
s=input()
po = re.findall(r'use strict[;]{0,1}', s)
print(po)