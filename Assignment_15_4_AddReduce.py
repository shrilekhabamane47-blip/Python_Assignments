from functools import reduce

Add=lambda A,B:A+B

def main():
    InputList=[]

    print("Enter no of elements want to add in List")
    Size=int(input())

    print("Enter the elements: ")
    for i in range(Size):
        Value=int(input())
        InputList.append(Value)
    Addition=reduce(Add,InputList)
    print("Addition is :",Addition)

if __name__=="__main__":
    main()