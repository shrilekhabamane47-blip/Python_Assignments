#Write a program which accepts one number and checks whether it is perfect number or not.
def CheckPerfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        return True
    else:
        return False
def main():
    No = int(input("Enter a Number : "))
    result = CheckPerfect(No)
    if result == True:
        print(No, "is a Perfect Number")
    else:
        print(No, "is Not a Perfect Number")
if __name__ == "__main__":
    main()