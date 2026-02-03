#Write a program which accepts a file name from the user and counts how many lines are present in the file

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
    
    for line in fobj:
        Count=Count+1
    fobj.close()
    print(f"Total Lines in file is {Count}")  
        
def main():
   Filename=input("Enter Filename :")
   CountLine(Filename) 
if __name__=="__main__":
    main()