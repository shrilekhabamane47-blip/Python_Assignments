#Write a lambda function which accepts one number and returns True if number is even otherwise False

CheckEven=lambda No: True if (No%2==0) else False
def main():
    Value=0
    Ret=False

    print("Enter a number:")
    Value=int(input()) 

    Ret=CheckEven(Value)
    
    if(Ret==True):
        print("It is Even")
    else:
        print("It is Odd")
if __name__ == "__main__":
    main()
