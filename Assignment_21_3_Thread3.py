#Design a Python application where multiple threads update a shared variable.Use a Lock to avoid race conditions.Each thread should increment the shared counter multiple times.Display the final value of the counter after all threads complete execution.

import threading

iCnt = 0
lobj = threading.Lock()

def Update():
    global iCnt
    for _ in range(20):
        with lobj:   
            iCnt = iCnt + 1
            print("Value of icnt ",iCnt,"updated by",threading.current_thread().name)
def main():
    global iCnt
    iCnt = 0   

    
    t1 = threading.Thread(target=Update, name="Thread-1")
    t2 = threading.Thread(target=Update, name="Thread-2")
    t3 = threading.Thread(target=Update, name="Thread-3")

    
    t1.start()
    t2.start()
    t3.start()

    
    t1.join()
    t2.join()
    t3.join()

    
    print("Final Value of iCnt is:", iCnt)

if __name__ == "__main__":
    main()
