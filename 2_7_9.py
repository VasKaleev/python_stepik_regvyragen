import re 
s=input()
#po = re.findall(r'\b[\d]{2}.[\d]*[ -][\d]*.[\d]*\b', s)
po = re.findall(r'0x[A-Fa-f0-9]{40}', s)
print(po)