class Tringle:
    def __init__(self,base,height): #use (constructor)
        self.base=base
        self.height=height

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Area = ", area)


T1 = Tringle(10,20)
T1.calculate_area()

T2 = Tringle(20,30)
T2.calculate_area() 

