#Write a program which accepts one number and prints that many numbers in reverse order
def PrintReverseRange(num):
    for i in range(num, 0, -1):
        print(i, end=" ")
def main():
    No = int(input("Enter a Number : "))
    PrintReverseRange(No)   
if __name__ == "__main__":
    main()