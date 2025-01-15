# ark = ["1","2","3","4","5"]
#
# ark = list(map(int,ark))
#
# print(ark)
#
# # def sq(a):
# #     return a*a
# # num = [1,2,3,4,5,6,7]
# # square = list(map(sq,num))
# # print(square)
#
# num = [1,2,3,4,5,6,7,8]
#
# square = list(map(lambda x : x*x , num))
# print(square)




def square(a):
    return a*a

def cube(a):
    return a*a*a

fun = [square,cube]

for i in range(5):
    val = list(map(lambda x:x(i), fun))
    print(val)