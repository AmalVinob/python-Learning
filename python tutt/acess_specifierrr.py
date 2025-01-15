# public -
# privated - __private (ptivate hsd 2 underscore in front)
# protected - _proctect (proctected has underscore in front) only accces by its below class also


class employee:
    employe_no = 8
    _proctected = 9
    __private = 98

    def employ(self):
        return f"name is {self.name}. salary is {self.salary}. type is {self.type} "

    def __init__(self, name, salary,type):
        self.name = name
        self.salary = salary
        self.type = type

enu = employee("amal",20000,"hr")
print(enu._proctected) #can only acces by the class
# print(enu.__private)   we can't print this it is only acceble in the class
print(enu._employee__private) # we can use this to print private contents - called - name mamling
