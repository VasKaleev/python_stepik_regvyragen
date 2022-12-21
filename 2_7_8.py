import re 
s=input()
#po = re.findall(r'\b[\d]{2}.[\d]*[ -][\d]*.[\d]*\b', s)
po = re.findall(r'\b[\d]{2}.[\d]* [-\d]*.[\d]*\b', s)
print(po)