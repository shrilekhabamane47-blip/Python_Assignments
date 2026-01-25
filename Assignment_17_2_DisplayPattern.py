# Write a program which accept one number and display below pattern.
#   *  *   *    *   *
#   *  *   *    *   *
#   *  *   *    *   *
#   *  *   *    *   *
#   *  *   *    *   *

def DisplayPattern():
    for i in range(5):
        for j in range(5):
            print("*",end="\t")
        print()
def main():
    DisplayPattern()
if __name__=="__main__":
    main()