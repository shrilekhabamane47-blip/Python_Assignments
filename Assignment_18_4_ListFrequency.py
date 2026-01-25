#Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List

def ListFrequency(InputList,Num):
    Icnt=0
    for i in range (len(InputList)):
        if Num==InputList[i]:
            Icnt=Icnt+1
    return Icnt

def main():

    Size=0
    Frequency=0
    IList=list()
    print("Enter size of list")
    Size=int(input())

    print("Enter elements of list")
    for i in range (Size):
        Value=int(input())
        IList.append(Value)

    print("Enter Number to search")
    No=int(input())

    Frequency=ListFrequency(IList,No)
    print("Frequency of Number in List :",Frequency)

    
if __name__=="__main__":
    main()
