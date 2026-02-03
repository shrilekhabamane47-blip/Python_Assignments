#Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.
import sys
import os
def CopyFile(Filename,Filename2="Demo.txt"):
    
    if os.path.isfile(Filename) and os.path.exists(Filename):
        
       
        fobj1=open(Filename,"r")
        fobj2=open(Filename2,"w")

        Data=fobj1.read()
        fobj2.write(Data)

        print("File Copied successfully")

        
        fobj1.close()
        fobj2.close()
            
    else:
        print("It's not a file or if its a file then its not exists")    

        


def main():
    if len(sys.argv) != 2:
        print("Invalid Number of Arguments")
    else:
        InputFile=sys.argv[1]
        CopyFile(InputFile)
        

if __name__=="__main__":
    main()