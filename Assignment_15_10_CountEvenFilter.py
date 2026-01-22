#Write a lambda function using filter () which accepts a list of numbers and returns the count of even numbers.

from functools import reduce

CheckEvenCount= lambda No: No%2==0

def main():

    InputList=[]

    print("Enter Number of element in list")
    Size=int(input())

    print("Enter elements in list :")
    for i in range(Size):
        Value=int(input())
        InputList.append(Value)

    EvenCount=len(list(filter(CheckEvenCount,InputList)))
    print("Count of even number:",EvenCount)


if __name__=="__main__":
    main()

