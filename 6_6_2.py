import re,sys
str = sys.stdin.read()
#test3 = re.findall(r'([a-z]+)', str)
test3 = re.findall(r'^(?:[\^\$])*', str)
print(test3) 
