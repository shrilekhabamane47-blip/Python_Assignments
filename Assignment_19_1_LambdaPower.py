#Write a program which contains one lambda function which accepts one parameter and return power of two
Power=lambda No:(No**2)

def main():
    Value=0
    Ret=0
    print("Enter a Number : ")
    Value=int(input())
    ret=Power(Value)
    print("Power of 2 for number is : ",ret)
if __name__ == "__main__":
    main()