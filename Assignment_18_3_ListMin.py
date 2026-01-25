# Write a program which accept N numbers from user and store it into List. Return Minimum number from that List
def ListMin(InputList):
    Min=InputList[0]
    for i in range (len(InputList)):
        if Min > InputList[i]:
            Min=InputList[i]
    return Min
def main():

    Size=0
    Min=0
    IList=list()
    print("Enter size of list")
    Size=int(input())

    print("Enter elements of list")
    for i in range (Size):
        Value=int(input())
        IList.append(Value)
    Min=ListMin(IList)
    print("Minimum element from list is :",Min)
if __name__=="__main__":
    main()