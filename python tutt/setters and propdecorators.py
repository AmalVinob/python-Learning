# class Employee:
#     def __init__(self,fname, lname):
#         self.fname = fname
#         self.lname = lname
#         self.email = f"{fname}.{lname}@codewithamal.com"
#
#     def explain(self):
#         return f"this employee is {self.fname} {self.lname}"
#
#     def print_email(self):
#         pass
#
# hindustani_supporter = Employee("hindustani","supporter")
# nikhil_raj_pandey = Employee("nikhil", "raj")
#
# print(hindustani_supporter.email)
#
# hindustani_supporter.fname = "us"
# print(hindustani_supporter.email) #not changed because  it is created in runtime


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


hindustani_supporter = Employee("hindustani","supporter")
# nikhil_raj_pandey = Employee("nikhil", "raj")

print(hindustani_supporter.explain())

print(hindustani_supporter.email)

hindustani_supporter.fname = "us"
print(hindustani_supporter.email)

hindustani_supporter.email = "this.that.@amal.com"
print(hindustani_supporter.email)

del hindustani_supporter.email

print(hindustani_supporter.email)