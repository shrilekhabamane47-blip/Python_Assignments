# Write a program which accepts length and width of rectangle and prints area.


def AreaRectangle(length, width):
    area = length * width
    return area

def main():
    Length = float(input("Enter the Length of the Rectangle: "))
    Width = float(input("Enter the Width of the Rectangle: "))
    result = AreaRectangle(Length, Width)
    print(f"The Area of the Rectangle is:", result)
if __name__ == "__main__":
    main()