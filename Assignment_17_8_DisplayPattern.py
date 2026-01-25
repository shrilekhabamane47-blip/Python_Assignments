# Write a program which accept one number and display below pattern
''' 
1
1       2
1       2       3
1       2       3       4
1       2       3       4       5
       
'''
def DisplayPattern():
    for i in range(1,6):
        for j in range(1,i):
            print(j,end="\t")
        print(i)
def main():
    DisplayPattern()
if __name__=="__main__":
    main()
