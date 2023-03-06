class phone:
    def __int__(self):
        print("I am in Iphone class")



class samsung(phone):
    def __int__(self):
        super().__int__()
        print("I am in samsung class")

s = samsung()
