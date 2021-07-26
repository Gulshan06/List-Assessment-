class department:
  def __init__(self,name,roll,adm,clg,mob):
    self.name = name
    self.roll = roll
    self.adm = adm
    self.clg = clg 
    self.mob = mob
  def display(self,):
    print(self.name, self.roll,self.adm,self.clg,self.mob)
a = input("name ")
b =int(input("roll "))
c =int(input ("adm "))
d =input("clg name ")
e = int(input("mob "))
p=department(a,b,c,d,e)
p.display()
