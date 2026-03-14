import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(Datapath):
    Border ="-"*40

    #Step 1 : Load the dataset from CSV file

    print(Border)
    print("Step 1 : Load the dataset from CSV file")
    print(Border)

    df = pd.read_csv(Datapath)

    print(Border)
    print("Some entries from dataset")
    print(df.head())
    print(Border)

    # Step 2: Clean Dataset by Removing Empty row

    print(Border)
    print("Step 2: Clean Dataset by Removing Empty row")
    print(Border)

    df.dropna(inplace = True)
    print("Total Records : ",df.shape[0])
    print("Total columns :",df.shape[1])
    print(Border)

    #Step 3: Separate independent and dependent Variable
    print(Border)
    print("Step 3: Separate independent and dependent Variable")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input columns : ",X.columns.to_list())
    print("Output columns : Class")

    #Step 4: Split the dataset for training and testing
    print(Border)
    print("Step 4: Split the dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(Border)
    print(" Information of Training and Testing Data")
    print("X_train shape : ",X_train.shape)
    print("Y_train shape : ",Y_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_test shape : ",Y_test.shape)
    print(Border)

    #Step 5 : Feature scaling
    print(Border)
    print("Step 5 : Feature scaling")
    print(Border)

    scalar = StandardScaler()

    #Independent Variable scaling
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)
    print("Feature Scaling is done")

    # Step 6 : Explore the multiple values of K
    # Hyper parameter tunning (K)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_pred =model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)
    print(Border)
    print("Accuracy report of all K values from 1 to 20 ")
    for value in accuracy_scores:
        print(value)
    print(Border)

    #Step 7 : plot the graph of K vs Accuracy
    print(Border)
    print("Step 7 : plot the graph of K vs Accuracy")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker = 'o')
    plt.title("K values vs Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()

def main():
    Border ="-"*40

    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()