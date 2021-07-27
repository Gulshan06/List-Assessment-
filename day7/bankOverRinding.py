class RBI:
    def IRate(self):
        print('8%')
class SBI(RBI):
    def IRate(self):
        print('10%')
class UCO(RBI):
    def IRate(self):
        print("7%")
obj1=RBI()
obj2=SBI()
obj3=UCO()
obj1.IRate()
obj2.IRate()
obj3.IRate()


