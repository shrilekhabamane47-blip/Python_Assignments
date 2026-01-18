#Write a program which accepts one number and prints square of that number.
def Square(num):
    return num * num
def main():
    No = int(input("Enter a Number : "))
    result = Square(No)
    print("Square of", No, "is :", result)

if __name__ == "__main__":
    main()