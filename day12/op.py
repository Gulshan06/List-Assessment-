import timeit
li = [2,34,5,6,74,43,56,67,76,56,43,4,56,67]
def f1():
    filter(5,li)
def f2():
    for i in li:
        if i == 42:
            pass
# def forloop():
#     for i in range(1000):
#         pass
# def whileloop():
#     n=0
#     while(n<=1000):
#         n+=1
#         pass

# print(timeit.timeit(forloop,number=100000))
# print(timeit.timeit(whileloop,number=100000))
print(timeit.timeit(f1,number=1))
print(timeit.timeit(f2,number=1))