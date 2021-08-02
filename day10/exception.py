# a = int(input())
# b = int(input())
try:
    a = int(input())
    b = int(input())
    div = a/b
    print(div)

except ZeroDivisionError:
    print("you enter wrong input")

except ValueError:
    print("only number is accepted ")
else:
    print("Done")

finally:
    print("thank you!!")



