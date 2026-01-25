#Write a program which accept one number from user and return its factorial.

def Factorial(num):
    fact=1
    for i in range(1, num + 1):
        fact=fact*i
    return fact
def main():
    No = int(input("Enter a Number : "))
    result = Factorial(No)
    print("Factorial of", No, "is:", result)
if __name__ == "__main__":
    main()