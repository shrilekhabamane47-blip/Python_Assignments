#Write a lambda function which accepts two numbers and returns addition.

Add=lambda No1,No2:No1+No2
def main():
    print("Enter first number:")
    Value1=int(input())

    print("Enter second number:")
    Value2=int(input())

    Result=Add(Value1,Value2)
    print("Addition is:",Result)
if __name__=="__main__":
    main()