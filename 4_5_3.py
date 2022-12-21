import re
s=input()
res_func = re.sub(r'([0-9]+)',lambda x: str(int(x[0])**2),s)
print(res_func)  

