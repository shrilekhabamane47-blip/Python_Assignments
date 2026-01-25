#Design a Python application that creates two threads named EvenFactor and OddFactor.Both threads should accept one integer number as a parameter.The EvenFactor thread should:Identify all even factors of the given number.Calculate and display the sum of even factors.The OddFactor thread should:Identify all odd factors of the given number.Calculate and display the sum of odd factors.After both threads complete execution, the main thread should display the message: "Exit from main"

import threading
import time
def SumEvenFactors(num):
    Factor=0
    for i in range(1, num):
        if num % i == 0 and i % 2 ==0:
            Factor=Factor+i
    print("Addition of Even Factor",Factor)

def SumOddFactors(num):
    Factor=0
    for i in range(1, num):
        if num % i == 0 and i % 2 !=0:
            Factor=Factor+i
    print("Addition of Odd Factor",Factor)


def main():

    No=int(input("Enter number to calculate Addition of even and odd factors : "))
    
    t1=threading.Thread(target=SumEvenFactors,args=(No,))
    t2=threading.Thread(target=SumOddFactors,args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
       
    print("Exit from main")
    
if __name__ == "__main__":
    main()