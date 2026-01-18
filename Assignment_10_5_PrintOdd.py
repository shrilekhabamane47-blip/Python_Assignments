#Write a program which accepts one number and prints all odd numbers till that number.
def PrintOddNumbers(num):
    for i in range(num + 1):
        if i % 2 != 0:
            print(i, end=" ")
def main():
    No = int(input("Enter a Number : "))
    PrintOddNumbers(No)
if __name__ == "__main__":
    main()