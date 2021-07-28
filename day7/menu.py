def Addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
a=int(input("enter a number:"))
b=int(input("enter a number:"))
while(True):
    print("select an option from menu:")
    print("\n")
    print("1.addition")
    print("2.substraction")
    print("3.multiply")
    choice=int(input("enter your choice:"))
    if(choice==1):
        print(Addition(a,b))
        break
    elif(choice==2):
        print(Subtraction(a,b))
        break
    else:
        print("exit")
        break