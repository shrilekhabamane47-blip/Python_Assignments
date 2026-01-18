#Write a program which accepts one number and prints reverse of that number
def ReverseNumber(num):
    rev = 0
    while num != 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = int(num / 10)
    return rev
def main():
    No = int(input("Enter a Number : "))
    result = ReverseNumber(No)
    print("Reverse of Number is", result)
if __name__ == "__main__":
    main()