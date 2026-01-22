#Write a lambda function which accepts one number and returns cube of that number

Cube=lambda No:(No*No*No)

def main():
    Value=0
    Ret=0
    print("Enter a Number :")
    Value=int(input())
    Ret=Cube(Value)
    #Ret=(lambda No:(No*No*No))(Value)
    print("Cube of Number is :",Ret)

if __name__ == "__main__":
    main()
