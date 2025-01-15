# # lambda is a function or anonymus function
#
#
# def minus(x, y):
#     return x-y
# print(minus(6,7))
# #or
#
# minuss = lambda x, y: x-y
#
# print(minuss(6,7))



# def a_first(a):
#     return a[1]

a= [[1,6], [5,6], [8,23]]
a.sort(key=lambda x:x[1])
print(a)