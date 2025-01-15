# # class student:
# #     pass
# #
# # amal = student()
# # larry = student()
# #
# # amal.name = "amal" #instance variable
# # amal.std = "degree"
# # print(amal.std)
# #
#
#
# class employee:
#         employe_no = 8
#
# harry = employee()
# print(harry.employe_no) #class variable
#
# print(employee.__dict__)
# employee.employe_no = 10
#
# print(employee.__dict__)

class employee:
    employe_no = 8

    def employ(self):
        return f"name is {self.name}. salary is {self.salary}. type is {self.type} "

    def __init__(self, name, salary,type):
        self.name = name
        self.salary = salary
        self.type = type

amal = employee("amal", 8500, "god boy")
# amal.name = "amal"
# amal.salary =8500
# amal.type = "good boy"

# print(amal.name,amal.salary,amal.type)
#
print(amal.__dict__)

# print(amal.employ())

