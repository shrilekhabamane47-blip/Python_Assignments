#Design a Python application that creates two separate threads named Even and Odd.The Even thread should display the first 10 even numbers.The Odd thread should display the first 10 odd numbers.
import threading
import time
def SumEven(No):
    
    for i in range(2,No+1,2):
        print(i)

def SumOdd(No):
    
    for i in range(1,No+1,2):
        print(i)


def main():
    start_time=time.time()
    t1=threading.Thread(target=SumEven,args=(20,))
    t2=threading.Thread(target=SumOdd,args=(20,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
       
    
    
if __name__ == "__main__":
    main()