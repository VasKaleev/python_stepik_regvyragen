import re
s = input()
#pattern = r'\b[Нн]ет|[Дд]а\s|[Нн]аверное'
pattern = r'\b(?:[Нн]ет|[Дд]а|[Нн]аверное)\b'
it = re.findall(pattern,s)
print(*it)
