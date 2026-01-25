# Write a program which accept one number form user and return addition of its factors.
def AddFactors(num):
    Factor=0
    for i in range(1, num):
        if num % i == 0:
            Factor=Factor+i
    return Factor
def main():
    FactorAdd=0
    No = int(input("Enter a Number : "))
    FactorAdd=AddFactors(No)
    print("Addition of Factors of number=",FactorAdd)
if __name__ == "__main__":
    main()