#Write a program which accept number from user and check whether that number is positive or negative or zero.
def CheckNumber(Num):
    if Num >= 0:
        if Num == 0:
            print("Zero")
        else:
            print("Positive Number")   
    else:
        print("Negative Number")
    
    
def main():
    print("Enter Number: ")
    No=int(input())
    CheckNumber(No)
    
if __name__=="__main__":
    main()
