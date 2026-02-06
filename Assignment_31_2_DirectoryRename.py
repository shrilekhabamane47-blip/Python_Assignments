#Design automation script which accept directory name and two file extensions from user. Rename all files with first file extension with the second file extenntion.

import sys
import Assignment_31_2_Module as AM

def main():
    Border ="-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

    if(len(sys.argv) != 4):
        print("Invalid Number of Aguments")
        print("Please Specify Directory name")
        return
    
    AM.DirectoryFilesRename(sys.argv[1],sys.argv[2],sys.argv[3])
    
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

if __name__ == "__main__":
    main()