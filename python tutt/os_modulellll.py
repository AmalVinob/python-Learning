import os  #built in module for - file rename , directry , open file etcccccccccc

print(dir(os))
"""
. some function's of os 
. can change current working directory
. after changing a directry we cant open a file of orginal directory.
. we can list the folders and files in a directry by using os.listdir()
. to make a directory we use mkdir
. to make maky directorys we use os.makedirs("this/that")
. we can rename the file by using os.rename("old name","new name")

"""
# print(os.getcwd()) # current working directry --- C:\Users\amalv\PycharmProjects\python tutt
# os.chdir("c://")
print(os.getcwd())
# f = open("amal.txt")

print(os.listdir())
# print(os.listdir("c://"))
# print(type(os.listdir("c://")))

# os.mkdir("this")
# os.makedirs("this/that")
# os.rename("amal.txt","amalvinob.txt")

# print(os.environ.get("PATH"))
# print(os.path.join("c://", "amal1.txt"))
# print(os.path.exists("c://Program Files"))
# print(os.path.isfile("c://Program Files"))
# print(os.path.isdir("c://Program Files"))