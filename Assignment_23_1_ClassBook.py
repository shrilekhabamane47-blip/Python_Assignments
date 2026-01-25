class BookStore:
    NoOfBook=0
    
    def __init__(self,N,A):
        self.Name=N
        self.Author=A
        BookStore.NoOfBook=BookStore.NoOfBook+1
    
    def Display(self):
        print(f"{self.Name}by{self.Author} .No of Book : {BookStore.NoOfBook}")


obj1=BookStore("Linux System Programming "," Robert Love")
obj1.Display()

obj2=BookStore("C programming "," Dennis Ritchie ")
obj2.Display()

        
