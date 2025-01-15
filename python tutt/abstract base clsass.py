# from abc import ABCMeta,abstractmethod
from abc import ABC,abstractmethod

# class Shape(metaclass=ABCMeta):
#     @abstractmethod
#     def print_area(self):
#         return 0

class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle "
    side = 4
    def __init__(self):
        self.length = 7
        self.breadth = 6

    def print_area(self):
        return self.length * self.breadth


rect = Rectangle()
print(rect.print_area())

# obj = Shape() abstract base class cant be make to an object

"""
abc metaclass used for for basee class which forces the child classes to implement the function
"""