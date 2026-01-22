# Write a program which accept number from user and print that number of "*" on screen.
def Print(No):
    for i in range(No+1):
        print("*",end=" ")
def main():
    print("Enter Number: ")
    No=int(input())
    Print(No)
if __name__=="__main__":
    main()