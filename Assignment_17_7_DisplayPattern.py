#Write a program which accept one number and display below pattern
'''
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
'''
def DisplayPattern():
    for i in range(1,6):
        for j in range(1,6):
            print(j,end="\t")
        print()
def main():
    DisplayPattern()
if __name__=="__main__":
    main()