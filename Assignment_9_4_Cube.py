#Write a program which accepts one number and prints cube of that number.
def Cube(Num):
    return Num**3

def main():
    No=int(input("Enter a Number : "))
    result=Cube(No)
    print("Cube of",No,"is :",result)

if __name__ == "__main__":
    main()