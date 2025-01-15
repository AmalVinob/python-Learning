class A:
    def set(self):
        print("thhis is a method in class a")

class B(A):
    def set(self):
        print("thhis is a method in class b")

class C(A):
    def set(self):
        print("thhis is a method in class c")

class D(C,B):
    pass
#dont use multiple inheritance

a = A()
b = B()
c = C()
d = D()


d.set()