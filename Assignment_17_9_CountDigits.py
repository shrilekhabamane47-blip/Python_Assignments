# Write a program which accept number from user and return number of digits in that number
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