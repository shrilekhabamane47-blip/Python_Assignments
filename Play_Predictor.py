import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def PlayPredictor(Datapath):
    Border ="-"*40

    #---------------------------------------
    #Step 1 : Load the dataset from CSV file
    #---------------------------------------

    print(Border)
    print("Step 1 : Load the dataset from CSV file")
    print(Border)

    df = pd.read_csv(Datapath)

    print(Border)
    print("Some entries from dataset")
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

    le = LabelEncoder()

    df['Whether'] = le.fit_transform(df["Whether"])
    df["Temperature"] = le.fit_transform(df["Temperature"])
    print(df)

    
    #---------------------------------------------------
    #Step 3: Separate independent and dependent Variable
    #---------------------------------------------------

    print(Border)
    print("Step 3: Separate independent and dependent Variable")
    print(Border)

    X = df[['Whether','Temperature']]
    Y = df['Play']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input columns : [Whether , Temprature]")
    print("Output columns : [Play]")

    #---------------------------------------------------
    #Step 4: Split the dataset for training and testing
    #---------------------------------------------------
    print(Border)
    print("Step 4: Split the dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    
    print(Border)
    print(" Information of Training and Testing Data")
    print("X_train shape : ",X_train.shape)
    print("Y_train shape : ",Y_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_test shape : ",Y_test.shape)
    print(Border)
    
    #---------------------------------------------------
    #Step 5: Deciding value of k to check accuracy
    #---------------------------------------------------

    print("Decide value of K")
    k=int(input())
    CheckAccuracy(X_train, X_test, Y_train, Y_test,k)
    #Step 5 : Feature scaling
    print(Border)
    print("Step 5 : Model Selection Training  and Deciding value of K")
    print(Border)

    #---------------------------------------------------
    #Step 6: Model Evaluation and Check Accuracy 
    #---------------------------------------------------

def CheckAccuracy(X_train, X_test, Y_train, Y_test,k):   #k=5 accuracy 100 , k=3 accuracy 83.33
    Border = "-"*40
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train,Y_train)
    Y_pred =model.predict(X_test)

    print(Border)
    print("Predicted values for test is ",Y_pred)
    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of KNN for Play prediction : ",accuracy*100)
    print(Border)
    
  
def main():
    Border ="-"*40

    print(Border)
    print("Play Prediction using KNN")
    print(Border)

    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()