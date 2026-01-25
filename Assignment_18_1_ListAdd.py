# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

def Listadd(ListAdd):
    Ans=0
    for i in range (len(ListAdd)):
        Ans=Ans+ListAdd[i]
    return Ans


def main():
    InputList=list()
    Size=0
    Value=0
    Result=0
    print("Enter Number of elements want to add in list")
    Size=int(input())

    print("Enter Elements in list")
    for i in range(Size):
        Value=int(input())
        InputList.append(Value)
    Result=Listadd(InputList)
    print("Addition of List of elements is :",Result)
if __name__=="__main__":
    main()

