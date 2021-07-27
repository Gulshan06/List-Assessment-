class person:
    def __init__(self,name):
        self.MyName = name
    def sayMyName(self):
        print(self.MyName)
a = input("enter your name : ")
p = person(a)
p.sayMyName()