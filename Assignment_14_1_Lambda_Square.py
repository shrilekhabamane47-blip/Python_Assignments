#Write a lambda function which accepts one number and returns square of that number

Square=lambda No:(No*No)

def main():
    Value=0
    Ret=0
    print("Enter a Number : ")
    Value=int(input())
    ret=Square(Value)
    print("Square of number is : ",ret)
if __name__ == "__main__":
    main()