#Design automation script which accept directory name and delete all duplicate files from that directory.

import sys
import Assignment_32_3_Module as AM

def main():
    Border ="-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of Aguments")
        print("Please Specify Directory name")
        return
    
    AM.DeleteDuplicate(sys.argv[1])
    
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

if __name__ == "__main__":
    main()