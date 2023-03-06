#parent class ,super class ,base class
#child class ,sub class ,derived class
class phone:
    def call(self):     #def  is A (Method)
        print("you can call  now")

    def message(self):
        print("you can message me now")

class Iphone(phone):  #(Using Inheritance )
    #Call,Message come through Inherite(phone clas)
    def photo(self):
        print("you can take photo ")

p = Iphone()
p.call()
p.message()
p.photo()
print(issubclass(Iphone,phone))
