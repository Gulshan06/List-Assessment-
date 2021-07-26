class India:
    def alotNum(self,num):
        print(num)
class carManufacturer(India):
    def makeCar(self,brand,color,price):
        print(brand,color,price)

class seller(carManufacturer):
    def customerOrder(self, name,mob):
        print(name,mob)
objind = India()
objman = carManufacturer()
objseller = seller()
objseller.customerOrder("ram",90)
objseller.makeCar("audi","blue","60lac")
objseller.alotNum("mp07")