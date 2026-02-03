#Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

import os
def CheckWord(Filename,word):

    if not os.path.exists(Filename):
        print("File not found")
        return
    if not os.path.isfile(Filename) :
        print("This not a file")
        return
    
    fobj=open(Filename,"r")
    
    for line in fobj:
        Words=line.split()
        for j in Words:
            if j == word:
                return True
            else:
                return False
    fobj.close()
    
        
def main():
    Filename=input("Enter Filename :")
    Word=input("Enter Word to search :")
    Ret=CheckWord(Filename,Word) 

    if Ret == True:
       print("Given word is present in file")
    else:
       print("Word not present in file")

if __name__=="__main__":
    main()