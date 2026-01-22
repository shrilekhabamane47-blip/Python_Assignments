#Write a lambda function which accepts three numbers and returns largest number

Large=lambda No1,No2,No3: No1 if No1>No2 and No1>No3 else No2 if No2>No3 and No2>No1 else No3
def main():
    print("Enter first number:")
    Value1=int(input())

    print("Enter second number:")
    Value2=int(input())

    print("Enter third number:")
    Value3=int(input())

    Result=Large(Value1,Value2,Value3)
    print("Largest number is:",Result)
if __name__=="__main__":
    main()