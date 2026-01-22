#Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.

def Divisible(Num):
    if Num % 5 == 0:
        return True
    else:
        return False
def main():

    print("Enter Number: ")
    No=int(input())

    Result=Divisible(No)

    print(Result)

if __name__=="__main__":
    main()
