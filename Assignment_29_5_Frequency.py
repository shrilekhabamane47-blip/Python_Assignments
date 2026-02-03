#Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file
import os
def Frequency(Filename,word):

    if not os.path.exists(Filename):
        print("File not found")
        return
    if not os.path.isfile(Filename) :
        print("This not a file")
        return
    Count=0
    fobj=open(Filename,"r")
    fobj.read()
    for line in fobj:
        Words=line.split()
        for j in Words:
            if j == word:
                Count=Count+1
    fobj.close()
    print(f"Total frequency of {word} in file is {Count}")  
        
def main():
   Filename=input("Enter Filename :")
   Word=input("Enter Word to search :")
   Frequency(Filename,Word) 
if __name__=="__main__":
    main()