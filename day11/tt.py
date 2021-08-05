
import time,re
# current_time=time.localtime()
# #print(current_time)
# current_clock_time=time.strftime("%y/%m/%d-%H:%M:%S")
# print(current_clock_time)
Name=input("enter")
price=input("enter")
def valid_product(Name,price):
    val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",Name)
    val2=re.match("[0-9]{0,7}$",price)
    if val1 and val2:
        return True
    else:
        return False
print(valid_product(Name,price))
