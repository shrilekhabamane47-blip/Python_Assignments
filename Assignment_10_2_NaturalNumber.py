#Write a program which accepts one number and prints sum of first N natural numbers.
def NaturalNumberSum(num):
    sum=0
    for i in range(1, num + 1):
        sum=sum+i
    return sum
def main():
    No = int(input("Enter a Number : "))
    result = NaturalNumberSum(No)
    print("Sum of Natural numbers is:", result)
if __name__ == "__main__":
    main()