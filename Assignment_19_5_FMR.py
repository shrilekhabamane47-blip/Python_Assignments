#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers.
from math import sqrt
from functools import reduce
def ChkPrime(num):  
    if num <= 1:
        return False
    
    for i in range(2, int(sqrt(num)) + 1) :
        if num % i == 0:
            return False
    return True

Multiply=lambda A:A*2
Max=lambda A,B: A if A>B else B


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

    FData= list(filter(ChkPrime,Data)) 
    print("Data After filter is : ",FData)

    MData= list(map(Multiply,FData))
    print("Data After Map is : ",MData)

    RData= reduce(Max,MData)
    print("Data After reduced is : ",RData)
   
if __name__=="__main__":
    main()