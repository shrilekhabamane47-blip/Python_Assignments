# Assignment 22 Program:3

class Arithmetic:
   
    def __init__(self):
        self.Value1=0
        self.Value2=0
    
    def Accept(self):
        print("Enter Value1 :")
        self.Value1=int(input())
        print("Enter Value2 :")
        self.Value2=int(input())

    def Addition(self):
        Arithmetic.Result= self.Value1+self.Value2
        return Arithmetic.Result
    
    def Subtraction(self):
        Arithmetic.Result=  self.Value1-self.Value2
        return Arithmetic.Result
    
    def Multiplication(self):
        Arithmetic.Result=  self.Value1*self.Value2
        return Arithmetic.Result
    
    def Division(self):
        try:
            Arithmetic.Result=  self.Value1/self.Value2
            return Arithmetic.Result
        except:
            print("Division by 0 error")
    def Display(self):
        print("Addition:", self.Addition())
        print("Subtraction:", self.Subtraction())
        print("Multiplication:", self.Multiplication())
        print("Division:", self.Division())

Aobj1=Arithmetic()
Aobj2=Arithmetic()

Aobj1.Accept()
Aobj2.Accept()

Aobj1.Display()
Aobj2.Display()



