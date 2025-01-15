class A:
    clsvar1 = "i am  a class variable in class A "
    def __init__(self):
        self.var1 ="i am inside class A's constructure"
        self.clsvar1 = "Instance variable in class A"
        self.special = "i am a special vaiable !!!!"

class B(A):
    clsvar1 = "i am in side class B "
    def __init__(self):

        self.var1 ="i am inside class A's constructure"
        self.clsvar1 = "Instance variable in class B"
        super().__init__()
        print(super().clsvar1)

a = A()
b = B()
print(b.clsvar1)
print(b.special)


#when something is overwrited then it wont run for eg __init__ in both class.... so we use super variable