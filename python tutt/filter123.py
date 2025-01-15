list1 = [1,2,3,4,5,6,7,8,9,10]
def greater_5(num):
    return num>5

grthan5 = list(map(greater_5,list1))
print(grthan5)

grthan5 = list(filter(greater_5,list1))
print(grthan5)

grthan5 = list(filter(lambda x:x>5,list1))
print(grthan5)