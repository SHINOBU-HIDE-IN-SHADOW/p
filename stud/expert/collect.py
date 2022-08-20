# from collections import Counter
# a = "aaabbbccccc"
# c = Counter(a)
# print(c)
# # print(c.type())
# from collections import namedtuple
# a = namedtuple('q','v,c')
# x = a(1,2)
# print(x.c)
# from collections import defaultdict
# a=defaultdict(int)
# a['a'] = 1
# a['b'] = 3
# x =a.values()
# print(x.elements())
from collections import deque
a = deque([13])
a.append([1,2,5])
a.append([7,9,10])
a.rotate(0)
a= list(a)
print(a[1].count(2))