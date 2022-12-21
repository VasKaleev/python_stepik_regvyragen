import re
""" 
def func(m):
    return str(len(m[0]))
res_func = re.sub(r'[a-zA-Z]{1,}', func, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
res_lambda = re.sub(r'[a-zA-Z]{1,}', lambda m: str(len(m[0])),
                    'Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
print(res_func)  # 5 5 2 6 5 4 2 3 8 3 11 8.
print(res_func == res_lambda)  # True """
m=input()
def func(m):
    return str(len(m[0]))
print(m[0])