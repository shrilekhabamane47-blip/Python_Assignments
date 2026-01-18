#Write a program which accepts one number and prints sum of digits
def SumDigits(num):
    sum = 0
    while num != 0:
        digit = num % 10
        sum = sum + digit
        num = int(num / 10)
    return sum
def main():
    No = int(input("Enter a Number : "))
    result = SumDigits(No)
    print("Sum of Digits are", result)
if __name__ == "__main__":
    main()

