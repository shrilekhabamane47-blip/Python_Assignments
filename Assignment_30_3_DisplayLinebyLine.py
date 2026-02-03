#Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
import os
def CountLine(Filename):

    if not os.path.exists(Filename):
        print("File not found")
        return
    if not os.path.isfile(Filename) :
        print("This not a file")
        return
    Count=0
    fobj=open(Filename,"r")
    print(f"--------------Below are contents of {Filename}------------------")
    for line in fobj:
        print(line)
    fobj.close()
    
        
def main():
   Filename=input("Enter Filename :")
   CountLine(Filename) 
if __name__=="__main__":
    main()