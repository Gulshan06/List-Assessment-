num = 10 
a = num.__add__(10)
print(a)

class Employee:
    def __init__(self):
        self.name='Ram'
        self.salary=10000
    def __str__(self):
        return 'name='+self.name+' salary='+str(self.salary)
e = Employee()
print(e)