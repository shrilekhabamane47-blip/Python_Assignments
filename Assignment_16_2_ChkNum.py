#Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.

def ChkNum(Num):
    if Num % 2 == 0:
        return True
    else:
        return False
def main():

    print("Enter Number: ")
    No=int(input())

    Result=ChkNum(No)

    if Result == True:
        print("Even Number")
    else:
        print("Odd Number")

if __name__=="__main__":
    main()
