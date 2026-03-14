import numpy as np
import matplotlib.pyplot as plt

def LinearRegresstionStudy():

    Border = "-"*40
    #---------------------------------------
    # Step 1 : Dataset
    #---------------------------------------
    
    X = [1, 2, 3, 4, 5]  
    Y = [50, 55, 60, 65, 70]  

    print(Border)
    print("Independent variable (X):", X)
    print("Dependent variable (Y):", Y)
    print(Border)

    #---------------------------------------
    # Step 2 :  Calculating Mean
    #---------------------------------------
    
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print(Border)
    print("Mean of X:", mean_X)
    print("Mean of Y:", mean_Y)
    print(Border)


    n = len(X)
    #---------------------------------------
    # Step 3 : Calculate slope (m)
    #---------------------------------------
    numerator = 0
    denominator = 0
    for i in range(n):
        numerator = numerator + (X[i] - mean_X) * (Y[i] - mean_Y)
        denominator = denominator+(X[i] - mean_X) ** 2
    m = numerator / denominator

    print(Border)
    print("Slope (m):", m)
    print(Border)

    #---------------------------------------
    # Step 4 : Calculate intercept (C)
    #---------------------------------------

    C = mean_Y - (m * mean_X)

    print(Border)
    print("Intercept (C):", C)
    print(Border)


    #---------------------------------------
    # Step 5  : Predict marks for 6 study hours
    #---------------------------------------
    x_new = 6
    y_pred = m * x_new + C

    print(Border)
    print(f"Predicted Marks for {x_new} study hours: {y_pred}")
    print(Border)



    x = np.linspace(1,6,n)
    y = C + m * x

    plt.plot(x,y,color = 'g',label = "Regression Line")
    plt.scatter(X,Y,color = 'r', label ="Scattor Plot")
    plt.scatter(x_new, y_pred, color='b',label="Prediction (6, 75)")



    plt.xlabel(" X : Independent Variable")
    plt.ylabel("Y : Dependent variables")

    plt.legend()
    plt.show()

def main():
    LinearRegresstionStudy()

if __name__ == "__main__":
    main()