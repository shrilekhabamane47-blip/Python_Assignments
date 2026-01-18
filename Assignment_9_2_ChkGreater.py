#Write a program which contains one function named as ChkGreater() which accepts two number and print greater number.
def ChkGreater(num1, num2):
    if num1>num2:
        return num1
    else:
        return num2
def main():
    No1=int(input("Enter First Number : "))
    No2=int(input("Enter Second number : "))
    result = ChkGreater(No1,No2)
    print("Greater number is :",result)       
if __name__ == "__main__":
    main()
    