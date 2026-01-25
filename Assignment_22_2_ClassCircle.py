# Assignment 22 Program:2

class Circle:

    Pi=3.14
    def __init__(self):
        self.Radius =0.0
        self.Area=0.0
        self.Circumference=0.0
    def Accept(self):
        self.Radius=float(input("Enter Radius :"))
    def CalculateArea(self):
        self.Area=Circle.Pi * self.Radius**2
    def CalculateCircumference(self):
        self.Circumference=2*Circle.Pi*self.Radius
    def Display(self):
        print("Radius of cirle :",self.Radius)
        print("Area of Circle is :",self.Area)
        print("Circumference of Circle is : ",self.Circumference)
    
cobj1=Circle()
cobj2=Circle()
cobj3=Circle()

cobj1.Accept()
cobj1.CalculateArea()
cobj1.CalculateCircumference()
cobj1.Display()

cobj2.Accept()
cobj2.CalculateArea()
cobj2.CalculateCircumference()
cobj2.Display()

cobj3.Accept()
cobj3.CalculateArea()
cobj3.CalculateCircumference()
cobj3.Display()