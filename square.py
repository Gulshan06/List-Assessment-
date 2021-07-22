n1 = int(input())
n2 = int(input())
n3 = int(input())
li = [n1,n2,n3]
def square(num):
    return num**2
print(list(map(square,li)))