#Design a Python application that creates two threads named Prime and NonPrime.Both threads should accept a list of integers.The Prime thread should display all prime numbers from the list.The NonPrime thread should display all non-prime numbers from the list
from math import sqrt
import threading
def ChkPrime(num):  
    if num <= 1:
        return None
    for i in range(2, int(sqrt(num)) + 1) :
        if num % i == 0:
            return False
    return True
def Prime(ListNumber):
    print("Prime Numbers are :",end="   ")
    for i in ListNumber:
        if ChkPrime(i):
            print(i,end="   ")

def NotPrime(ListNumber):
    print("Not Prime Numbers are :",end="   ")
    for i in ListNumber:
        result= ChkPrime(i)
        if result==False:
            print(i,end="   ")

def main():

    Size=0
    
    IList=list()
    print("Enter size of list")
    Size=int(input())

    print("Enter elements of list")
    for i in range (Size):
        Value=int(input())
        IList.append(Value)
    
    t1=threading.Thread(target=Prime,args=(IList,))
    t2=threading.Thread(target=NotPrime,args=(IList,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
if __name__=="__main__":
    main()
