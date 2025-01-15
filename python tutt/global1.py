# l = 10
# def function1(n):
#     # global l
#     l = 5
#     print(n, "i have printed")
#     print(l)
#
# function1("this is me")
# print(l)

x = 89
def amal():
    x = 10
    def anu():
        global x
        x=5
    print("before calling anu ", x)
    anu()
    print("after calling anu",x)
amal()
print(x)