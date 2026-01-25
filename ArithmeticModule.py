def Add(num1, num2):
    addition = num1 + num2
    return addition  
def Sub(num1, num2):
    subtraction = num1 - num2
    return subtraction
def Mult(num1, num2):
    multiplication = num1 * num2
    return multiplication
def Div(num1, num2):
    division = num1 / num2 if num2 != 0 else "Divide by Zero Error"
    return division