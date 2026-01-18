#Write a program which accepts one number and checks whether it is divisible by 3 and 5.
def Divisible(Num):
    if(Num % 3 ==0) and (Num % 5 ==0):
        return True
    else:
        return False
def main():
    No = int(input("Enter a Number : "))
    result = Divisible(No)
    if result == True:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")
if __name__ == "__main__":
    main()
