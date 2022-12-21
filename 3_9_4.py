import re
s=input()
pat = r'(?<=>)[^<>]+?(?=<)'
p = re.findall(pat,s)
p="".join(p) 
p=p.replace(" ","")
p=" ".join(p)    
print(p)        
