#Write a program which accepts two file names from the user.Fir st file is an existing file. Second file is a new fileCopy all contents from the first file into the second file.
import os
def CopyDynamic(Filename1,Filename2):

    if not os.path.exists(Filename1):
        print("File not found")
        return
    if not os.path.isfile(Filename1) :
        print("This not a file")
        return
    
    fobj1=open(Filename1,"r")
    fobj2=open(Filename2,"w")

    Data=fobj1.read()
    fobj2.write(Data)

    print(f"Contents from {Filename1} is copied to {Filename2}")
    fobj1.close()
    fobj2.close()

    
        
def main():
    Filename1=input("Enter Source Filename :")
    Filename2=input("Enter Destination Filename :")
    
    CopyDynamic(Filename1,Filename2) 

if __name__=="__main__":
    main()