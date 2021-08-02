try:
    a = int(input())
    if a<0:
        raise ValueError
    else:
        print(a)
except ValueError:
    print(a,'out of range')


