import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousPredictor():
    # Load the data
    Exp = [1,2,3,4,5]
    Salary = [20000,25000,30000,35000,40000]

    print("Values of independent variable : Experience - ",Exp)
    print("Values of independent variable : Salary - ",Salary)
    SumX = 0
    SumY=0
    n = len(Exp)
    

    for i,j in zip(Exp,Salary):
        SumX = SumX+i
        SumY=SumY+j

    Mean_Exp = SumX/n
    Mean_Salary = SumY/n

    print("X_MEAN is : ",Mean_Exp)    #3.0
    print("Y_MEAN is : ",Mean_Salary)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator =numerator + ((Exp[i]-Mean_Exp) * (Salary[i] - Mean_Salary)) 
        denominator = denominator + ((Exp[i]-Mean_Exp)**2) 
    m=numerator/denominator

    print("Slope of line is m : ",m) 

    C = Mean_Salary-(m*Mean_Exp) 
    print("Y intercept of line i.e. C ",C)

    yp = []
    for i in Exp:
        yp.append(m * i + C)
    print("Predicted Values : ",yp)
    
    Experience = 6
    Predicted_salary = m*Experience+C
    print("Predicted salary for", Experience, "years of experience is :", Predicted_salary)
    Sum=0
    for i in range(n):
        Sum = Sum + (Salary[i]-yp[i])**2
    print("Sum of residual: ",Sum)

    MSE = Sum /n
    print("Mean Squared error is :",MSE)

    SS_total=0
    for i in range(n):
        SS_total = SS_total+(Salary[i]-Mean_Salary)**2
    
    R2 = (1-(Sum/SS_total))
    print("R square is :",R2)

    x = np.linspace(1,6,n)
    y = C + m * x

    plt.plot(x,y,color = 'g',label = "Regression Line")
    plt.scatter(Exp,Salary,color = 'r', label ="Scattor Plot")

    plt.xlabel(" Experience : Independent Variable")
    plt.ylabel("Salary : Dependent variables")

    plt.legend()
    plt.show()
def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()