#Write a program which accepts two file names through command line arguments and compares the contents of both files.
import os
import sys
def CompareFile(File1,File2):
    if not (os.path.exists(File1) and os.path.exists(File2)):
        print("File not found")
        return
    if not (os.path.isfile(File1) and os.path.isfile(File2)):
        print("This not a file")
        return
    fobj1=open(File1,"r")
    fobj2=open(File2,"r")

    if(fobj1.read()== fobj2.read()):
        print("Both files have same content")
    else:
        print("File content is different")    
               
def main():
    if (len(sys.argv)<3):
        print("Invalid number of arguments ")
    else:
        File1=sys.argv[1]
        File2=sys.argv[2]
        CompareFile(File1,File2)
if __name__=="__main__":
    main()