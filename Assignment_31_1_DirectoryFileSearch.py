#Design automation script which accept directory name and file extension from user. Display all files with that extension.
import sys
import Assignment_31_1_Module as AM

def main():
    Border ="-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid Number of Aguments")
        print("Please Specify Directory name")
        return
    
    AM.DirectoryFileSearch(sys.argv[1],sys.argv[2])
    
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

if __name__ == "__main__":
    main()