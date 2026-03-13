import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def SalesAdvertise(Datapath):
    Border = "-"*40
    #---------------------------------------
    # Step 1 :Load Dataset
    #---------------------------------------

    print(Border)
    print("Step 1 : Load Dataset")
    df = pd.read_csv(Datapath)
    print("Few records from the Dataset")
    print(df.head())
    print(Border)

    #---------------------------------------
    # Step 2 :Remove Unwanted columns
    #---------------------------------------

    print(Border)
    print("Step 2: Remove unwanted columns")
    print(Border)

    print("Shape of dataset before removal",df.shape)
    

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)
    print("Shape of dataset after removal",df.shape)

    print(Border)
    print("Clean Dataset is")
    print(Border)
    print(df.head())

    #--------------------------------------------------------------
    # Step 3 : Split dataset into independent and dependent variable
    #--------------------------------------------------------------

    print(Border)
    print("Step 3 : Split dataset into independent and dependent variable")
    print(Border)

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of independent variable ",X.shape)
    print("Shape of dependent variable ",Y.shape)

    #--------------------------------------------------
    # Step 4 : Split dataset for Training and Testing
    #--------------------------------------------------

    print(Border)
    print("Step 4 : Split dataset for Training and Testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_test shape ",X_train.shape)
    print("X_test shape ",X_test.shape)
    print("Y_test shape ",Y_train.shape)
    print("Y_test shape ",Y_test.shape)

    #--------------------------------------------------
    # Step 5 : Create and Train the Model
    #--------------------------------------------------

    print(Border)
    print("Step 5 : Create and Train the Model")
    print(Border)

    model = LinearRegression()
    model.fit(X_train,Y_train)

    #--------------------------------------------------
    # Step 6 : Test the Model
    #--------------------------------------------------

    print(Border)
    print("Step 6 :  Test the Model")
    print(Border)

    Y_pred = model.predict(X_test)

    
    #--------------------------------------------------
    # Step 7 : Predicted sales of according advertise
    #--------------------------------------------------

    print(Border)
    print("Step 10 : Predicted sales of according advertise")
    print(Border)

    Result = pd.DataFrame({
        'Actual Sale':Y_test.values,
        'Predicted Sale ':Y_pred
        })
    print(Result.head())

def main():
    SalesAdvertise("Advertising.csv")

if __name__ =="__main__":
    main()