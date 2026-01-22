#Write a lambda function which accepts one number and returns True if number is odd otherwise False

CheckOdd=lambda No:True if No%2!=0 else False
def main():
    Value=0
    Ret=False

    print("Enter a number:")
    Value=int(input()) 

    Ret=CheckOdd(Value)
    
    if(Ret==True):
        print("It is Odd")
    else:
        print("It is Even")
if __name__ == "__main__":
    main()