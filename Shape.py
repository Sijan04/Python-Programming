class Shape:
    def __int__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am area method of shape class")

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area :",area)


class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area :", area)

t1 = Triangle(10,20)
t1.area()

r1 = Rectangle(20,40)
r1.area()