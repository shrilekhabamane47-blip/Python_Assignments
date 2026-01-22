#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

def Add(Num1,Num2):
    return Num1 + Num2
def main():

    print("Enter First Number: ")
    No1=int(input())
    print("Enter Second Number: ")
    No2=int(input())

    Result=Add(No1,No2)

    print("Addititon is ",Result)
if __name__=="__main__":
    main()
