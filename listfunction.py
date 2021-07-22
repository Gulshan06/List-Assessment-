large = []
small = []
num1 = int(input())
num2 = int(input())
def largelist(num1,num2):
    if (num1>num2):
        large.append(num1)
        small.append(num2)
    else:
        small.append(num1)
        large.append(num2)
largelist(num1,num2)
print(large)
print(small)
