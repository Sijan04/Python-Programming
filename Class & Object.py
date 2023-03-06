class Student:
    roll=""
    cgpa=""

    def set_value(self,roll,cgpa):
        self.roll=roll
        self.cgpa=cgpa

    def display(self):
       print(f"Roll : {self.roll},CGPA :{self.cgpa}")


Sijan = Student()
Sijan.set_value(101,3.44)
Sijan.display()


Sabbir = Student()
Sabbir.set_value(105,3.99)
Sabbir.display()

