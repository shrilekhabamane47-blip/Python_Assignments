#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

from functools import reduce
FilterNum=lambda A:A>=70 and A<=90
Increase=lambda A:A+10
ProductElement=lambda A,B: A*B

def main():
    Size = 0
    Value = 0
    
    print("Enter the number of elements :")
    Size = int(input())

    Data = list()

    print("Enter the elements :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    print(Data)      

    FData= list(filter(FilterNum,Data)) 
    print("Data After filter is : ",FData)

    MData= list(map(Increase,FData))
    print("Data After Map is : ",MData)

    RData= reduce(ProductElement,MData)
    print("Data After reduced is : ",RData)
   
if __name__=="__main__":
    main()