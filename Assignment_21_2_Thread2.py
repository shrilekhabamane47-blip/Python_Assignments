#Design a Python application that creates two threads.Thread 1 should calculate and display the maximum element from an list.Thread 2 should calculate and display the minimum element from the same list.The list should be accepted from the user.
import threading

def ListMin(InputList):
    Min=InputList[0]
    for i in range (len(InputList)):
        if Min > InputList[i]:
            Min=InputList[i]
    print("Minimum No is :",Min)

def ListMax(InputList):
    Max=0
    for i in range (len(InputList)):
        if Max < InputList[i]:
            Max=InputList[i]
    print("Maximum Number is :",Max)

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
    
    t1=threading.Thread(target=ListMin,args=(IList,))
    t2=threading.Thread(target=ListMax,args=(IList,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
if __name__=="__main__":
    main()