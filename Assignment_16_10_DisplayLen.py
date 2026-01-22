#write a program which accept name from user and display length of its name
def DisplayLength(Name):
    icnt=0
    for i in Name:
        icnt=icnt+1
    return icnt
    
def main():
    print("Enter Name:")
    Name=input()

    Length=DisplayLength(Name)

    print("Length of Name is :",Length)
if __name__=="__main__":
    main()


