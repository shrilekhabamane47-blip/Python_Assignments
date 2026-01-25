import ArithmeticModule as obj
def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))
    
    addition=obj.Add(No1,No2)
    subtraction=obj.Sub(No1,No2)
    multiplication=obj.Mult(No1,No2)
    division=obj.Div(No1,No2)
    print("Addition :", addition)
    print("Subtraction :", subtraction)
    print("Multiplication :", multiplication)
    print("Division :", division)  
if __name__ == "__main__":
    main()