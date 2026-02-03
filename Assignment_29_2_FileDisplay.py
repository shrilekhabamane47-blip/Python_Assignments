#Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
import os
def FileDisplay(Filename):
    Ret = os.path.isfile(Filename)
    if Ret == True:
        
        fobj=open(Filename,"r")
        print("--------File is successfully open and below are file contents-------")
        Data=fobj.read()
        print(Data)
        fobj.close()
    else:
        print(f"{Filename} is not present")    

def main():

    Filename = input("Enter Filename : ")
    FileDisplay(Filename)
    
if __name__=="__main__":
    main() 