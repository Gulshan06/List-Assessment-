class Animals:
    def eyes(self,eye):
        self.eye=eye
        print(eye)
    def foots(self,foot):
        self.foot=foot
        print(foot)
class Dog(Animals):
    def dogcolor(self,color):
        self.color=color
        print(color)
objeye=Animals()
objcolor=Dog()
objcolor.foots(4)
objeye.eyes(2)
objcolor.dogcolor("Black")
