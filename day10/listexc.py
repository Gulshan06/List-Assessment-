# li = [1,3,4,56,7]
try:
    li = list(map(int, input().split()))
    print(li[10])
except (IndexError,NameError):
    print("index is out of range")