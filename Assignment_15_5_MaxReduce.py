#Write a lambda function using reduce ( ) which accepts a list of numbers and returns the maximum element.
from functools import reduce

Max=lambda A,B: A if A>B else B

def main():

    InputList=[]

    print("Enter Number of element in list")
    Size=int(input())

    print("Enter elements in list :")
    for i in range(Size):
        Value=int(input())
        InputList.append(Value)
    MaxNum=reduce(Max,InputList)
    print("Maximum Number is :",MaxNum)

if __name__=="__main__":
    main()