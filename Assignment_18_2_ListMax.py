#Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
def ListMax(InputList):
    Max=0
    for i in range (len(InputList)):
        if Max < InputList[i]:
            Max=InputList[i]
    return Max
def main():

    Size=0
    Max=0
    IList=list()
    print("Enter size of list")
    Size=int(input())

    print("Enter elements of list")
    for i in range (Size):
        Value=int(input())
        IList.append(Value)
    Max=ListMax(IList)
    print("Maximum element from list is :",Max)
if __name__=="__main__":
    main()