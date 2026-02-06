#Design automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt. 

import sys
import Assignment_32_2_Module as AM

def main():
    Border ="-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of Aguments")
        print("Please Specify Directory name")
        return
    
    AM.Duplicate(sys.argv[1])
    
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

if __name__ == "__main__":
    main()