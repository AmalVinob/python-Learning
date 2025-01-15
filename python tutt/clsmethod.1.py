# alter native constuctor

class employee:
    leaves = 9
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def printdetails(self):
        return f"name is {self.name}.age is {self.age}.salary is {self.salary}"

    #class method
    def change_leave(cls, new_leaves):
        cls.leaves = new_leaves

    #class method
    def from_str(cls, string):
        params = string.split("-")
        return cls(params[0],params[1],params[2])


amal = employee("amal",22,8000)
anu = employee("anu",21,9000)
athul = employee.from_str("athul-23-5000")

print(athul.slary)
employee.leaves = 10

amal.change_leave(35)

print(amal.salary,amal.leaves)
print(amal.printdetails())