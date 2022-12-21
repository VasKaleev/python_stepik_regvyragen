import re 
s = input()
#s = 'That wall was black'
#po = re.findall("^....", s)
#po = re.findall(r'\W\b\w\w\w\w\b\W', s)
#po = re.findall(r'\D\D\D\D\D', s)
po = re.findall(r'.....', s)
print(po)