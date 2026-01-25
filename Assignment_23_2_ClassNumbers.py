#assignment 23 Program 3
from math import sqrt
class Numbers:

    def __init__(self,No):
        self.Value=No

    def ChkPrime(self):  
        if self.Value <= 1:
            return None
        for i in range(2, int(sqrt(self.Value)) + 1) :
            if self.Value % i == 0:
                return False
        return True
  
    def Factors(self):
        print(f"Factors of {self.Value} are:")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total
    
    def ChkPerfect(self):
        return self.SumFactors() == self.Value

obj1=Numbers(10)
obj2=Numbers(11)

print("Number is Prime  :",obj1.ChkPrime())
print("Number is Perfect: ",obj1.ChkPerfect())
obj1.Factors()
print("Sum of factor ",obj1.SumFactors())


print("Number is Prime :",obj2.ChkPrime())
print("Number is Perfect: ",obj2.ChkPerfect())
obj2.Factors()
print("Sum of factor: ",obj2.SumFactors())


    
    
    
    