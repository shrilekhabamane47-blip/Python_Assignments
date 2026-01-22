#Write a lambda function using filter () which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

Divisible=lambda No: No%5==0 and No%3==0

def main():

    InputList=[]

    print("Enter Number of element in list")
    Size=int(input())

    print("Enter elements in list :")
    for i in range(Size):
        Value=int(input())
        InputList.append(Value)
    result=list(filter(Divisible,InputList))
    print("Numbers Divisible by 5 and 3 :",result)

if __name__=="__main__":
    main()
