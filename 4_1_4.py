import re
pattern = r'(?P<prot>https?):\/\/(?P<dom>[a-z.\d]*?)\/[a-z\/\d_-]*(?P<par>\?[^# ]*)?(?P<anchor>[#][a-z]*)?'
s=input()
it = re.finditer(pattern,s)
for i in it:
    print("Полная ссылка:",i.group())       
    print("Протокол:",i.group('prot'),'|',"Домен:",i.group('dom'),'|',"Параметры:",i.group('par'),'|',"Якорь:",i.group('anchor'))
    print()