# from itertools import product
# a =[1,2]
# b = [3,4]
# x = product(a,b, repeat=2)
# # print(list(x))
# from itertools import permutations
# a = [1,2,3]
# c= permutations(a,2)
# print(list(c)[1][1])
# from itertools import groupby
# a= [[1,2,3],[2,3,4],[5,6,7],[2,7,8],[7,8,9]]
# c=groupby(a,key=lambda x: 2 in x)
# for x,y in c:
#     print(x,list(y))
# from itertools import count,cycle,repeat
# for i in count(10):
#     print(i)
#     if i== 15:
#         break
from itertools import groupby
a= [[1,2,3],[2,3,4],[5,6,7],[2,7,8],[7,8,9]]
c=groupby(a,key=lambda x: x[0])
for x,y in c:
    print(x,list(y))