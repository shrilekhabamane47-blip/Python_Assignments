#Write a lambda function using filter () which accepts a list of numbers and returns a list of odd

CheckOdd=lambda No: No%2!=0

def main():
    print("Enter Number of elements in list")
    Size=int(input())
    InputList=[]
    print("Enter elements: ")
    for i in range(Size):
        Value=int(input())
        InputList.append(Value)
        OddList=list(filter(CheckOdd,InputList))
    print("Data after filtering Odd Number is :",OddList)

if __name__=="__main__":
    main()
