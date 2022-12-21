import re 
s=input()
#po = re.findall(r'\b([nN][a-z-].*?)\b',s)
po = re.findall(r"(?<!\S)[nN][A-z_-]*(?!\S)",s)
print(po)