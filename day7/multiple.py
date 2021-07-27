class AddationOperation:
    def addTwoNum(self,a,b):
        return a+b
class SubtractonOperation:
    def subTwoNum(self,a,b):
        return a-b
class multiplicationOperation:
    def mulTwoNum(self,a,b):
        return a*b
class calculator(AddationOperation,SubtractonOperation,multiplicationOperation):
    pass

obj1 = calculator()
a = int(input())
b = int(input())
# print(obj1.addTwoNum(a,b))
# print(obj1.mulTwoNum(a,b))
# print(obj1.subTwoNum(a,b))
print(issubclass(calculator,AddationOperation))
print(issubclass(AddationOperation,calculator))