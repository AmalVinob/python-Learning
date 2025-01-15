class employee:
    employe_no = 8

    def employ(self):
        return f"name is {self.name}. salary is {self.salary}. type is {self.type} "

    def __init__(self, name, salary,type):
        self.name = name
        self.salary = salary
        self.type = type

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"employee( {self.name} , {self.salary}, {self.type})"

    def __str__(self):
        return f"name is {self.name}. salary is {self.salary}. type is {self.type} "

emp1 = employee("amal",355,"programmer")
# emp2 = employee("anu",155,"manager")
# emp3 = employee("anu",200,"manager")

# print(emp1 + emp2)
# print(emp1 / emp2)

print(repr(emp1))

