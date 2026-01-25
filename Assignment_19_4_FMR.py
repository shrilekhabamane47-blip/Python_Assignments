#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

from functools import reduce
Even=lambda A:A % 2 ==0
Square=lambda A:A**2
Add=lambda A,B: A+B

def main():
    Size = 0
    Value = 0
    
    print("Enter the number of elements :")
    Size = int(input())

    Data = list()

    print("Enter the elements :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    print(Data)      

    FData= list(filter(Even,Data)) 
    print("Data After filter is : ",FData)

    MData= list(map(Square,FData))
    print("Data After Map is : ",MData)

    RData= reduce(Add,MData)
    print("Data After reduced is : ",RData)
   
if __name__=="__main__":
    main()