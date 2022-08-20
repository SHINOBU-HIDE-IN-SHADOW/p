# a = [1,2,3]
# b = a[1]
# x = iter(a)
# print(next(x))
# print(next(x))
# print(next(x))
def a(n):
    while n >0:
        yield n 
        n -=1
        # return n
x = a(4)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# def a(n):
#     while n >0:
#         yield n 
#         n -=1
# x = a(4)
# print(list(a(4)))
# # print(sum(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(list())