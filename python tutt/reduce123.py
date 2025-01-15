from functools import reduce

list1 = [1,5,6,7]

# num = 0
# for i in list1:
#     num = num + 2
# print(num)

prod = reduce(lambda x,y : x+y , list1)
print(prod)