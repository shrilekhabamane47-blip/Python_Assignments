#Design a Python application that creates two threads named Thread1 and Thread2.Thread1 should display numbers from 1 to 50.Thread2 should display numbers from 50 to 1 in reverse order.Ensure that:Thread2 starts execution only after Thread1 has completed.Use appropriate thread synchronization

import threading
lobj=threading.Lock()

def PrintForword():
    with lobj:
        for i in range(1,51):
            print(i)
def PrintReverse():
    with lobj:
        for i in range(50,0,-1):
            print(i)         

            
def main():
    
    
    t1=threading.Thread(target=PrintForword)
    t2=threading.Thread(target=PrintReverse)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ =="__main__":
    main()