#Write a program which accepts one number and checks whether it is palindrome or not
from Assignment_11_4_ReverseNumber import ReverseNumber


def IsPalindrome(num):
    original = num
    rev = 0
    '''while num != 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = int(num / 10)'''

    rev = ReverseNumber(num)
    if original == rev:
        return True
    else:
        return False
def main():
    No = int(input("Enter a Number : "))
    result = IsPalindrome(No)
    if result == True:
        print(No, "is a Palindrome Number")
    else:
        print(No, "is not a Palindrome Number")
if __name__ == "__main__":
    main()
   