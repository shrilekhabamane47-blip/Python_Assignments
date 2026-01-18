#Write a program which accepts one number and prints multiplication table of that number.
def MultiplicationTable(num):
    Result=0
    for i in range (1, 11):
        Result=num*i
        print(Result,end="  ")
def main():
    No = int(input("Enter a Number : "))
    MultiplicationTable(No)       
if __name__ == "__main__":
    main()