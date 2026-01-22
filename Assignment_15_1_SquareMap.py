#Write a lambda function using map ( ) which accepts a list of numbers and returns a list of squares of each number
Square = lambda No: No * No

def main():
    print("Enter Number of elements in list")
    Size=int(input())
    InputList=list()

    print("Enter the elements :")
    for i in range(Size):
        Value=int(input())
        InputList.append(Value)
    SquareList=list(map(Square,InputList))
    print("Data after Square :",SquareList)

if __name__=="__main__":
    main()