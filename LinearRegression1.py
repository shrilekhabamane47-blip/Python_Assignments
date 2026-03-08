import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousPredictor():
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of independent variable : X - ",X)
    print("Values of independent variable : Y - ",Y)
    SumX = 0
    SumY=0
    n = len(X)
    n = len(Y)

    for i,j in zip(X,Y):
        SumX = SumX+i
        SumY=SumY+j

    Mean_X = SumX/n
    Mean_Y = SumY/n

    print("X_MEAN is : ",Mean_X)    #3.0
    print("Y_MEAN is : ",Mean_Y)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator =numerator + ((X[i]-Mean_X) * (Y[i] - Mean_Y)) 
        denominator = denominator + ((X[i]-Mean_X)**2) 
    m=numerator/denominator

    print("Slope of line is m : ",m) 

    C = Mean_Y-(m*Mean_X) 
    print("Y intercept of line i.e. C ",C)

    yp = []
    for i in X:
        yp.append(m * i + C)
    print("Predicted Values : ",yp)
    
    x = 6
    y_pred = m* x +C
    print("Predicted value for x =6 is ",y_pred)
    
    Sum=0
    for i in range(n):
        Sum = Sum + (Y[i]-yp[i])**2
    print("Sum of residual: ",Sum)

    MSE = Sum /n
    print("Mean Squared error is :",MSE)

    SS_total=0
    for i in range(n):
        SS_total = SS_total+(Y[i]-Mean_Y)**2
    print(" (Y - Y_bar) ^2 is ",SS_total)

    R2 = (1-(Sum/SS_total))
    print("R square is :",R2)


def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()