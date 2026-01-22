#Write a lambda function using reduce ( ) which accepts a list of numbers and returns the product of all elements
from functools import reduce

ProductElement=lambda A,B: A*B

def main():

    InputList=[]

    print("Enter Number of element in list")
    Size=int(input())

    print("Enter elements in list :")
    for i in range(Size):
        Value=int(input())
        InputList.append(Value)
    Product=reduce(ProductElement,InputList)
    print("Product of number is :",Product)

if __name__=="__main__":
    main()