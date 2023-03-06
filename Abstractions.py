from abc import ABC,abstractmethod

class Shape(ABC):
    def __int__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area rectangle :", area)

obj = Rectangle(10,20)
obj.area()
