# # a = [2,1,5,4]
# # b = [3,2,6,5]
# # def d(x):
# #     return x
# # c = map(d,a*b)
# # print(list(c))
# # def a(x):
# #     return x+6
# # x = [1,2,3]
# # a = a(x)
# a = [1,2,3]
# b = [4,5,6]
# c =a*5
# print(a)
# print(b)
# print(c)
b = [1,2,3]
a = [round(x+x/2) for x in b]
print(a)