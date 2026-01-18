#Write a program which accepts one number and prints binary equivalent
def PrintBinary(num):
    if num > 1:
        PrintBinary(int(num / 2))
    print(num % 2, end="")
def main():
    No = int(input("Enter a Number : "))
    PrintBinary(No)
if __name__ == "__main__":
    main()