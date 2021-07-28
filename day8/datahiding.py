class A:
    __name='Gulshan'  # __name means hidden
    def test(self):
        print(__name)

obj = A()
# obj.test()
print(obj._A__name)
