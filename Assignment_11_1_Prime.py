#Write a program which accepts one number and checks whether it is prime or not.
import math

def IsPrime(num):  
    if num <= 1:
        return False
    #for i in range(2, int(num**0.5) + 1):
    for i in range(2, int(math.sqrt(num)) + 1) :
        if num % i == 0:
            return False
    return True
def main():
    No = int(input("Enter a Number : "))
    result = IsPrime(No)
    if result == True:
        print(No,"Prime Number")
    else:
        print(No, "Not a Prime Number")
if __name__ == "__main__":
    main()
   