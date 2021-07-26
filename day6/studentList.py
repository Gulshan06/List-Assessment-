class Students:
    def __init__(self,name,roll,admno):
        self.myname=name
        self.myrollno=roll
        self.admno=admno
obj=[]
obj.append(Students('Gulshan',21,432))
obj.append(Students('Gullu',21,432))
obj.append(Students('ram',21,432))
obj.append(Students('naveen',21,432))
print(obj[0].myname)
print(obj[1].myname)
print(obj[2].myname)
print(obj[3].myname)