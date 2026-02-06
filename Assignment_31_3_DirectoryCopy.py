#Design automation script which accept two directory names. Copy all files from first directory into second directory. 
import sys
import Assignment_31_3_Module as AM

def main():
    Border ="-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid Number of Aguments")
        print("Please Specify Directory name")
        return
    
    AM.DirectoryCopy(sys.argv[1],sys.argv[2])
    
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

if __name__ == "__main__":
    main()