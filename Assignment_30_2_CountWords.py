#Write a program which accepts a file name from the user and counts the total number of words in that file

import os
def CountWords(Filename):

    if not os.path.exists(Filename):
        print("File not found")
        return
    if not os.path.isfile(Filename) :
        print("This not a file")
        return
    Count=0
    fobj=open(Filename,"r")
    
    for line in fobj:
        Words=line.split()
        for j in Words:
            Count=Count+1
    fobj.close()
    print(f"Total number of words in file is {Count}")  
        
def main():
   Filename=input("Enter Filename :")
   CountWords(Filename) 
if __name__=="__main__":
    main()