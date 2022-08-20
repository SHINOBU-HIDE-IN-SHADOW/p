# print("Hello " + input("Heelo"))
# a = [4,6,8,7,9]
# print(isinstance(a,list))
class A:
    num = 50
    def __init__(self):
        self.num = 2
        print("a")
    def Hello(self):
        print("Hello")
class B(A):
    def __init__(self):
        print("b")
        self.Hello()
        super().Hello()
    def Hello(self):
        print("fuck")
class C(A):
    def __init__(self):
        A.__init__(self)
        print("b")
        self.Hello()
    @classmethod
    def x(cls):
        cls.num = 40
        print(cls.num)
a =B()
b =C()
b.x()

