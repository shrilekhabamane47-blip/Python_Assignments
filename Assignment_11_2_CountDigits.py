#Write a program which accepts one number and prints count of digits in that number
def CountDigits(num):
    count = 0
    while num != 0:
        count = count + 1
        num=int(num/ 10)
    return count
def main():
    No = int(input("Enter a Number : "))
    result = CountDigits(No)
    print("Count of Digits are", result)
if __name__ == "__main__":
    main() 