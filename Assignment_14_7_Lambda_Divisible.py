#Write a lambda function which accepts one number and returns True if divisible by 5

Divisible=lambda No: True if No%5==0 else False

def main():
    Value=0
    Ret=False

    print("Enter a number:")
    Value=int(input()) 

    Ret=Divisible(Value)
    
    if(Ret==True):
        print("It is divisible by 5")
    else:
        print("It is not divisible by 5")
if __name__ == "__main__":
    main()