class cars:
    color = "black"
    brand = "BMW"
    def findMileage(self,li,km):
        return km/li
myCar=cars()
a = input("enter color: ")
b = input("enter brand: ")
li = int(input('enter the litres '))
km = int(input("enter the km "))
mileage = myCar.findMileage(li,km)

myCar.color=a
myCar.brand=b
print(myCar.color)
print(myCar.brand)
# default value 
defaultcar=cars()
print(defaultcar.color)
print(defaultcar.brand)
print(mileage)