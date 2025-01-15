class Employee:
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithamal.com"

    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    @property #decorator
    def email(self):
        if self.fname == None or self.lname == None:
            return "email is not set"
        return f"{self.fname}.{self.lname}@codewithamal.com"

    @email.setter
    def email(self, string):
        print("setiing now")
        names = string.split("@")[0]
        self.fname = string.split(".")[0]
        self.lname = string.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill", "F")
print(skillf.email)
 # to know about the object more  we use object intro spection

print(type("sjkdhkasdahskd"))
print(id(skillf))
print(id("this is amal"))
print(type(skillf))
print(dir(skillf))

import inspect
class inspec:
    def ins(self):
        a = inspect.isclass(inspect)
        return a
        b = inspect.ismodule(inspect)
        return b

a = inspec()
print(a.ins())

b = inspec()
print(b.ins())
