#Write a program which accepts one number and prints that many numbers starting from 1
def PrintRangeOfNumbers(num):
    for i in range(1, num + 1):
        print(i, end=" ")
def main():
    No = int(input("Enter a Number : "))
    PrintRangeOfNumbers(No)
if __name__ == "__main__":
    main()