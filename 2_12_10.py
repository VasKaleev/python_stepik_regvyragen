import re 
s=input()
#po = re.findall(r'(?<!\w)(?:0\.[\d]{1,2})(?!\w)|(?:1(?=\s)|(?=$))|(?:0(?=\s)|(?=$))',s)
#po = re.findall(r'(?<!\w)(?:0\.[\d]{1,2})(?!\w)|[01]\s',s)
#po = re.findall(r'(?<!\w)(?:0\.[\d]{1,2})(?!\w)|[0-1](?=\s)',s)
#po = re.findall(r'(?<= )1(?= )')
po = re.findall(r'^(.*?)[ .]',s)
#(?!\.)
print(po)