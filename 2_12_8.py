import re 
s=input()
#po = re.findall(r'\b\w+[,]\s\b',s)
#po = re.findall(r'\b(\w+)[.,:?!;]\s\b',s)
po = re.findall(r'(\w+)[.,:?!;]',s)
print(po)