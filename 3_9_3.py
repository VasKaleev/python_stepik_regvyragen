#import click
import re
s1=input().split(" ")
s=input()
pat = s1[0]
rep = s1[1]
p = re.sub(pat,rep,s)
print(p)
#click.pause("Нажмите любую клавишу!")