class cal:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def floordiv(self,a,b):
        return a//b
calculate=cal()
a = int(input())
b = int(input())
print(calculate.add(a,b))
print(calculate.sub(a,b))
print(calculate.mul(a,b))
print(calculate.div(a,b))
print(calculate.floordiv(a,b))
