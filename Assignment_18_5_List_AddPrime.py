# Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().
from MarvellousNum import ChkPrime
def ListPrime(InputList):
    Ans=0

    for i in InputList:
        if ChkPrime(i):
            Ans=Ans+i
    
    return Ans

def main():

    Size=0
    Addition=0
    IList=list()

    print("Enter size of list")
    Size=int(input())

    print("Enter elements of list")
    for i in range (Size):
        Value=int(input())
        IList.append(Value)
    Addition=ListPrime(IList)
    print("Addition of prime numbers from list is :",Addition)

if __name__=="__main__":
    main()


