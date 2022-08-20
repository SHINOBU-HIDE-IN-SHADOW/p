# class A:
#     def __init__(self,x) -> 2:
#         print(x)
# def f(x) -> 123:
#     return x
# print(A)
# print(f.__annotations__['return']['docstring'])
# rd={'type':float,'units':'Joules',
#     'docstring':'Given mass and velocity returns kinetic energy in Joules'}
# def f()->rd:
#     pass
# f.__annotations__['return']['type']
# f.__annotations__['return']['units']
# f.__annotations__['return']['docstring']
def a():
    """ asdasdas
    asdasdas
    asdasda
    hello
    """
    #asdasqqqq
    return 5
print(a().__doc__) 
# help(a)