# from re import X


# class A:
#     def __init__(self,f):
#         self.num = 0
#         self.f = f

#     def __call__(self,*a,**b):
#         self.num += 1
#         print(f'{self.num}' )
#         return self.f(*a,**b)
        
# def Wrrap(x):
#     def w(*a,**b):
#         print("start")
#         print(x(*a,**b))
#         print(a)
#         print("end")
#     return w
# @Wrrap
# def adder(a,b):
#     return a+b
# adder(8,b=9)
# @A
# def adder(a,b):
#     return a+b
# @A
# def miner(a,b):
#     return a-b
# adder(2,2)
# adder(2,2)
# adder(2,2)
# adder(2,2)
# miner(5,1)
class A:
    def __init__(self):
        self.num = 0
    def __enter__(self):
        self.num+=1
    def __exit__(self,type, value, traceback):
        print(self.num)
with A():
    pass#중간
