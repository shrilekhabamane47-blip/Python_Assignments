# Write a lambda function which accepts two numbers and returns minimum number.

MinNo=lambda No1,No2:No1 if No1<No2 else No2

def main():
    print("Enter first number:")
    Value1=int(input())

    print("Enter second number:")
    Value2=int(input())

    Result=MinNo(Value1,Value2)
    print("Minimum number is:",Result)
if __name__=="__main__":
    main()  