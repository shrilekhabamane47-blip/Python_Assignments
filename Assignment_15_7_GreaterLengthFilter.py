# Write a lambda function using filter () which accepts a list of strings and returns a list of strings having length greater than 5.

GreaterLength=lambda A: len(A)>5

def main():

    InputList=[]

    print("Enter Number of element in list")
    Size=int(input())

    print("Enter elements in list :")
    for i in range(Size):
        Value=input()
        InputList.append(Value)
    GreaterLen=list(filter(GreaterLength,InputList))
    print("Length of string greater than 5 :",GreaterLen)

if __name__=="__main__":
    main()