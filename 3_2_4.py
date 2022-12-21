import re 
s='I love regex!'
Match = re.match(r'I love regex!',s)
print(Match.group(0))
print(Match.start())
print(Match.end())