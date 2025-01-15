n = int(input("enter the number : "))
def fun():
    bool = int(input("enter the boolian number : "))
    if bool == 1:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print("*", end="")
            print("\n")
    elif bool == 0:
        for i in reversed(range(1, n + 1)):
            for j in reversed(range(1, i+1)):
                print("*", end="")
            print("\n")
    else:
        print("write either 1 or 2 : ")
        fun()
fun()
# #
# # # *
# # # **
# # # ***
# # # ****
# # # *****
#
# n = int(input("enter the number : "))
# for i in reversed(range(1,n+1)):
#     for j in reversed(range(1,i+1)):
#         print("*",end="")
#     print("\n")