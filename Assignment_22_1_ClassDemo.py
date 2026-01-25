# Assignment  no 22 program: 1

class Demo:
    Value=10

    def __init__(self,Num1,Num2):
        self.No1=Num1
        self.No2=Num2
    def Fun(self):
        print("Value of instance variable from Fun:",self.No1,self.No2)
    def Gun(self):
        print("Value of instance variable from Fun:",self.No1,self.No2)


 
obj1=Demo(11,21)
obj2=Demo(51,101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()