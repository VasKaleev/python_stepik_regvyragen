import re
def get_x(m):
    return {'o': 'x', 'O':'X'}[m[0]]
print(re.subn(r'(o)', get_x, input(),flags=re.I)[0])