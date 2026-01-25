# Design a Python application that creates two threads.Thread 1 should compute the sum of elements from a list.Thread 2 should compute the product of elements from the same list.Return the results to the main thread and display them
import threading
Result={}
def Sum(List,Result):
    Ans=0
    for i in range (len(List)):
        Ans=Ans+List[i]
    Result["Sum"]=Ans
def Product(List,Result):
    Ans=1
    for i in range (len(List)):
        Ans=Ans*List[i]
    Result["Product"]=Ans

def main():
    InputList=list()
    Size=0
    Value=0
    Result={}
    print("Enter Number of elements want to add in list")
    Size=int(input())

    print("Enter Elements in list")
    for i in range(Size):
        Value=int(input())
        InputList.append(Value)
        
    t1=threading.Thread(target=Sum,args=(InputList,Result,))
    t2=threading.Thread(target=Product,args=(InputList,Result,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", Result["Sum"])
    print("Product of elements:", Result["Product"])


if __name__ =="__main__":
    main()