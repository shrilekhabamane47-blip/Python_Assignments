#Write a program which accepts marks and displays grade 
def DisplayGrade(marks):
    if marks > 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"
def main():
    Marks = float(input("Enter the Marks: "))
    grade = DisplayGrade(Marks)
    print("The Grade is:", grade)
if __name__ == "__main__":
    main()