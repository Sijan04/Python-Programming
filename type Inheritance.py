class A:
    def display1(self):  #def display is a method
        print("I am inside A class")
class B(A):
    #Display1()
    def display2(self):
        print("I am inside B class")

class C(B):
    # Display1()
    # Display2()
    def display3(self):
        super().display1() #by using super we call display 1 and display 2
        super().display2()
        print("I am inside C class")

obj = C()
obj.display3()



