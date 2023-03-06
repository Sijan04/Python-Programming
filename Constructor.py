class Student:
    roll=""
    cgpa=""

    def __init__(self,roll,cgpa): #use (constructor)
        self.roll=roll
        self.cgpa=cgpa

    def display(self):
       print(f"Roll : {self.roll},CGPA :{self.cgpa}")


Sijan = Student(303,4.00)
Sijan.display()


Sabbir = Student(304,3.99)
Sabbir.display()

