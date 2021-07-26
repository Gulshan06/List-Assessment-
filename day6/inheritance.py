class cars:
    def carcolor(self,color):
        self.color=color
        print(self.color)
class Bmw(cars):
    def carspeed(self,speed):
        self.speed=speed
        print(self.speed)
objcar = cars()
objBmw = Bmw()       
objBmw.carcolor('White')
objBmw.carspeed(180)


