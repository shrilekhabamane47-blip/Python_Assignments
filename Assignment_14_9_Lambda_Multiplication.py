#Write a lambda function which accepts two numbers and returns multiplication

Mul=lambda No1,No2:No1*No2 
def main():
    print("Enter first number:")
    Value1=int(input())

    print("Enter second number:")
    Value2=int(input())

    Result=Mul(Value1,Value2)
    print("Multiplication is:",Result)
if __name__=="__main__":
    main()