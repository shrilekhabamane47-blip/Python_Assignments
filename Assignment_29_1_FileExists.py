#Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

import os
def FileExist(Filename):
    Ret=os.path.exists(Filename)
    if Ret == True:
        if os.path.isfile(Filename):
            print("File is exists in current directory") 
        elif os.path.isdir(Filename):
            print("Its not file its a directory")
    else:
        print("File not exists in current directory")
      

def main():

    Filename = input("Enter Filename : ")
    FileExist(Filename)
    
if __name__=="__main__":
    main() 