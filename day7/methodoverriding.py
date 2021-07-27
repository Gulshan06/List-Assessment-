class car:
    def color(self):
        print('Red')

class Bmw(car):
    def color(self):
        print('white')
obj1=Bmw()
obj1.color()

obj2=car()
obj2.color()
