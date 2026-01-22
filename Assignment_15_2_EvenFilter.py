#Write a lambda function using filter () which accepts a list of numbers and returns a list of even

CheckEven=lambda No: No%2==0

def main():
    print("Enter Number of elements in list")
    Size=int(input())
    InputList=[]
    print("Enter elements: ")
    for i in range(Size):
        Value=int(input())
        InputList.append(Value)
    EvenList=list(filter(CheckEven,InputList))
    print("Data after filtering Even Number is :",EvenList)

if __name__=="__main__":
    main()

