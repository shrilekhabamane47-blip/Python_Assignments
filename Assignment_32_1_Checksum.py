#Design automation script which accept directory name and display checksum of all files.

import sys
import Assignment_32_1_Module as AM

def main():
    Border ="-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of Aguments")
        print("Please Specify Directory name")
        return
    
    AM.DirectoryScanning(sys.argv[1])

    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

if __name__ == "__main__":
    main()