#Write a program which accepts radius of circle and prints area of circle.
def AreaCircle(radius, pi=3.14):
    area = pi * (radius ** 2)
    return area
def main():
    Radius = float(input("Enter the Radius of the Circle: "))
    result = AreaCircle(Radius)
    print("The Area of the Circle is:", result)
if __name__ == "__main__":
    main()