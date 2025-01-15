f = open("amal.txt", "rt")
# content = f.read()
# # print("1.", content)
# #
# # content = f.read()
# # print("2.", content)
#
# for item in content :
#     print(item)

# for item in f:
#     print(item, end="")
#
# print(f.readline())
# print(f.readline())
# print(f.readline())

print(f.readlines())

f.close()