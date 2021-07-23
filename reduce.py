import functools
lis = [1,2,3,4]
print(functools.reduce(lambda a, b: a+b, lis))