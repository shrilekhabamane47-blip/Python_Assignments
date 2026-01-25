#Write a program which accept number from user and return addition of digits in that number
def AddDigits(num):
    sum = 0
    while num != 0:
        digit = num % 10
        sum = sum + digit
        num = int(num / 10)
    return sum
def main():
    No = int(input("Enter a Number : "))
    result = AddDigits(No)
    print("Sum of Digits are", result)
if __name__ == "__main__":
    main()
