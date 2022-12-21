import re,sys
""" string = '''
I like flags
I like flags
I like flags
''' """
str = sys.stdin.read()
#test1 = re.findall(r'^I like flags$', string, flags=re.MULTILINE)
#test2 = re.findall(r'^I like flags$', string, flags=re.M)
test3 = re.findall(r'(?m)^I like flags$', str)
print(test3) 

#import sys,re
#str = sys.stdin.read()
#test = re.findall(r'start[а-яА-ЯёЁa-zA-Z ].end', str,flags=re.DOTALL)
#test = re.findall(r'([a-zA-Z ]+)', str)
#print(test)
