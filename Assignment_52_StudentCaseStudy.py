
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    #--------------------------------
    # Step 1 : Load the Dataset
    #--------------------------------

    print("Step 1 : Load the Dataset")
    df = pd.read_csv("student-mat.csv",sep=";")

    print("First Few Records : ")
    print(df.head())

    print("Shape of Dataset")
    print(df.shape)

    print("Missing values from dataset")
    print(df.isnull().sum())

    #-------------------------------------
    # Step 2: Select Feature (Independent)
    #--------------------------------------

    print("Step 2: select Feature (Independent)")

    X= df[['G1','G2','G3','studytime','failures','absences']]

    print("Selected Feature  : ")
    print(X.head())
    
    print("Shape of selected features : ")
    print(X.shape)

    #-------------------------------------
    # Step 3: Scale the data
    #--------------------------------------
    print("Step 3: Scale the data")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print("Data after scaling : ")
    print(X_scaled[:5])

    #-------------------------------------
    # Step 5: Train and Test the model
    #-------------------------------------- 
    model = KMeans(n_clusters=3,random_state=42,n_init=10)
    clusters = model.fit_predict(X_scaled)
    df["clusters"]= clusters
    print("Dataset with cluster ")
    print(df.head(100))

    #-------------------------------------------------------------
    # Step 6: Result Visualization
    #-------------------------------------------------------------
    label_mapping= { 0: 'Top Performer',1:'Average Student',2:'Struggling Student'}
    df["Performance Group"] = df['clusters'].map(label_mapping)
    
    axes = plt.subplots(1, 3, figsize=(18,5))
   
    sns.scatterplot(x=df["G1"], y=df["failures"], hue=df["Performance Group"], s=80, ax=axes[0])
    axes[0].set_title("Cluster Visualization: G1 vs Failures")
    axes[0].set_xlabel("Grade 1 (G1)")
    axes[0].set_ylabel("Failures")

    
    sns.scatterplot(x=df["G2"], y=df["failures"], hue=df["Performance Group"], s=80, ax=axes[1])
    axes[1].set_title("Cluster Visualization: G2 vs Failures")
    axes[1].set_xlabel("Grade 2 (G2)")
    axes[1].set_ylabel("Failures")

    
    sns.scatterplot(x=df["G3"], y=df["failures"], hue=df["Performance Group"], s=80, ax=axes[2])
    axes[2].set_title("Cluster Visualization: G3 vs Failures")
    axes[2].set_xlabel("Final Grade (G3)")
    axes[2].set_ylabel("Failures")

    plt.show()


    plt.figure(figsize=(6,4))
    sns.barplot(x="Performance Group", y="studytime", data=df)
    plt.title("Average Study Time Vs Performance Group")
    plt.xlabel("Performance Group")
    plt.ylabel("Study Time")
    plt.show()

    
    plt.figure(figsize=(6,4))
    sns.barplot(x="Performance Group", y="absences", data=df)
    plt.title("Average Absences Vs Performance Group")
    plt.xlabel("Performance Group")
    plt.ylabel("Absences")
    plt.show()

    print(df.groupby('Performance Group')[['G3','studytime','failures','absences']].mean())
if __name__ == "__main__":
    main()