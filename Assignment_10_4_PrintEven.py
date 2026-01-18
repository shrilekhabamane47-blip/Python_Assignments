#Write a program which accepts one number and prints all even numbers till that number
def PrintEvenNumbers(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i, end=" ")
def main():
    No = int(input("Enter a Number : "))
    PrintEvenNumbers(No)
if __name__ == "__main__":
    main()