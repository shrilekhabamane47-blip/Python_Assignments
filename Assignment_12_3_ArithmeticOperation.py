#Write a program which accepts two numbers and prints addition, subtraction, multiplication and division
def ArithmeticOperations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Divide by Zero Error"
    return addition, subtraction, multiplication, division
def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))
    addition, subtraction, multiplication, division = ArithmeticOperations(No1, No2)
    print("Addition :", addition)
    print("Subtraction :", subtraction)
    print("Multiplication :", multiplication)
    print("Division :", division)  
if __name__ == "__main__":
    main()