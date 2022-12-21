import re 
s=input()
po = re.findall(r'\b[IVXLCDM]+\b', s)
print(po)