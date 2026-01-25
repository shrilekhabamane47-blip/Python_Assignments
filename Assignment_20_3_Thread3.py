#Design a Python application that creates two threads named EvenList and OddList.Both threads should accept a list of integers as input.Both threads should accept a list of integers as input.The EvenList thread should:Extract all even elements from the list Calculate and display their sum.The OddList thread should:Extract all odd elements from the list.Calculate and display their sum.Threads should run concurrently
import threading
def ChkEven(Num):
    Sum=0
    for i in Num:
        if i % 2 == 0:
            print("even",i)
            Sum=Sum+i
    print("Even sum",Sum)
def ChkOdd(Num):
    Sum=0
    for i in Num:
        if i % 2 != 0:
            print("odd",i)
            Sum=Sum+i
    print("odd sum",Sum)

def main():
    Size=0
    Value=0
    List=[]
    print("Enter Number of elements want to add in list")
    Size=int(input())

    print("Enter Elements in list")
    for i in range(Size):
        Value=int(input())
        List.append(Value)

    t1=threading.Thread(target=ChkEven,args=(List,))
    t2=threading.Thread(target=ChkOdd,args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
       
    print("Exit from main")
    
if __name__ == "__main__":
    main()