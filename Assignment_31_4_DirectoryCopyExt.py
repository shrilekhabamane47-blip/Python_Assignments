#Design automation script which accept two directory names and one file extension. Copy all files with the specified extension from first directory into second directory.

import sys
import Assignment_31_4_Module as AM

def main():
    Border ="-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

    if(len(sys.argv) != 4):
        print("Invalid Number of Aguments")
        print("Please Specify Directory name")
        return
    
    AM.DirectoryCopyExt(sys.argv[1],sys.argv[2],sys.argv[3])
    
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

if __name__ == "__main__":
    main()