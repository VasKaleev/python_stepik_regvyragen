import re 
#s = input()
s = 'That wall was black'
#po = re.findall("^....", s)
#po = re.findall(r'\W\b\w\w\w\w\b\W', s)
po = re.findall(r'\b[a-z][a-z][a-z][a-z]\b', s)
print(po)