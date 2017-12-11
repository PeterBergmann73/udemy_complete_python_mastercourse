# my_list = list(range(10))
#
# print(my_list)
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)
#
# r1 = range(10)
# iter1 = iter(r1)
# print(next(iter1))
#
# print(r1.index(5))
#
# odd = range(1, 10000, 2)
# print(odd[985])

# decimals = range(0, 100)
# print(decimals)
#
# my_range = decimals[3:40:3]
# print(my_range)
# print(my_range == range(3, 40, 3))
# print(range(0, 5, 2) == range(0, 6, 2))
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:
#     print(i)

o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)

for i in p:
    print(i)