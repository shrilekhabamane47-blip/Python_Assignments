import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report,precision_score,recall_score,f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

Border = "="*100
border1 = "-"*100
#---------------------------------------------------------------
# Step 1 :  Load the dataset 
#---------------------------------------------------------------
print(Border)
print("Step 1 :  Load the dataset")
print(Border)
df = pd.read_csv("diabetes.csv")
print("Shape of dataset ",df.shape)
print(border1)
print("First Five records of Dataset : ")
print(border1)
print(df.head())


#---------------------------------------------------------------
# Step 2 : Data Analysis (EDA)
#---------------------------------------------------------------

print(Border)
print("Step 2 : Data Analysis ")
print(Border)

print("Information of columns of dataset")
print(border1)
print(df.info())
print(border1)
print("Missing values count :")
print(border1)
print(df.isnull().sum())
print(border1)
print("Statistical report of dataset")
print(border1)
print(df.describe())


#---------------------------------------------------------------
# Step 3 : Data Visualization
#---------------------------------------------------------------

print(Border)
print("Step 3 : Data Visualization")
print(Border)

print("Histogram of Outcome")
plt.figure(figsize=(8,5))
plt.hist(df['Outcome'])
plt.title("Histogram of Outcome")
plt.xlabel("Outcome (0 = Non-diabetic, 1 = Diabetic)")
plt.ylabel("Frequency")
plt.show()

print(" Boxplot of Outcome")
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Outcome'])
plt.title("Boxplot of Outcome")
plt.xlabel("Outcome")
plt.show()

print("Pairplot with Outcome")
sns.pairplot(df, hue="Outcome", diag_kind="hist") 
plt.suptitle("Pairplot of Features by Outcome", y=1.02)
plt.show()


#---------------------------------------------------------------
# Step 4 : Data Preprocessing and Scaling
#---------------------------------------------------------------
print(Border)
print("Step 4 : Data Preprocessing and Scaling")
print(Border)

Feature = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
df[Feature] = df[Feature].replace(0, np.nan)
df[Feature] = df[Feature].fillna(df[Feature].median())
print(df.isnull().sum())


print(border1)
print("Split Dataset into Feature and Label")
print(border1)
X = df.drop("Outcome", axis=1)
Y = df["Outcome"]
print("Shape of Independent Variable ",X.shape)
print("Shape of Independent Variable ",Y.shape)


print(border1)
print("Scale Dataset using standard scaler")
print(border1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("Standard Scaled Data):\n", X_scaled[:5])

#---------------------------------------------------------------
#Step 5: Split the dataset for training and testing
#---------------------------------------------------------------
print(Border)
print("Step 5: Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test=train_test_split(X_scaled,Y,test_size=0.2,random_state=42)

#----------------------------------------------------------
#Step 6 : create base models
#----------------------------------------------------------
print(Border)
print("Step 6: create base models")
print(Border)
model_lr  = LogisticRegression(max_iter=800)
model_dt = DecisionTreeClassifier(random_state=42)
model_knn = KNeighborsClassifier(n_neighbors=5)

#----------------------------------------------------------
#Step 7 : Train base models
#----------------------------------------------------------
print(Border)
print("Step 7 : Train base models")
print(Border)

model_lr.fit(X_train, Y_train)
model_dt.fit(X_train, Y_train)
model_knn.fit(X_train, Y_train)

#-------------------------------------------------------------
# Step 8: Test  model
#-------------------------------------------------------------

print(Border)
print("Step 8 : Test base models")
print(Border)
y_pred_lr = model_lr.predict(X_test)
y_pred_dt = model_dt.predict(X_test)
y_pred_knn = model_knn.predict(X_test)

#-------------------------------------------------------------
# Step 9: Evaluate  model
#-------------------------------------------------------------
print(Border)
print("Step 9: Evaluate  model Performance")
print(Border)

print("Accuracy of models")
print("Logistic Regression Accuracy:", accuracy_score(Y_test, y_pred_lr))
print("Decision Tree Accuracy:", accuracy_score(Y_test, y_pred_dt))
print("KNN Accuracy:", accuracy_score(Y_test, y_pred_knn))

print(border1)
print("Precision of models")
print(border1)
print("Logistic Regression Precision:", precision_score(Y_test, y_pred_lr))
print("Decision Tree Precision:", precision_score(Y_test, y_pred_dt))
print("KNN Precision:", precision_score(Y_test, y_pred_knn))

print(border1)
print("Recall of models")
print(border1)
print("Logistic Regression Recall Score:", recall_score(Y_test, y_pred_lr))
print("Decision Tree Recall Score:", recall_score(Y_test, y_pred_dt))
print("KNN Recall Score:", recall_score(Y_test, y_pred_knn))

print(border1)
print("Model's F1 Score ")
print(border1)     
print("Logistic Regression F1_Score:", f1_score(Y_test, y_pred_lr))
print("Decision Tree F1_Score:", f1_score(Y_test, y_pred_dt))
print("KNN F1_Score :", f1_score(Y_test, y_pred_knn))

print(border1)
print("Confusion Matrix : ")
print(border1)
print("Logistic Regression Confusion Matrix:")
print(confusion_matrix(Y_test, y_pred_lr))
print("Decision Tree Confusion Matrix:") 
print(confusion_matrix(Y_test, y_pred_dt))
print("KNN Confusion Matrix :")
print(confusion_matrix(Y_test, y_pred_knn))
print(border1)

#-------------------------------------------------------------
# Step 10: Visualization
#-------------------------------------------------------------
print(Border)
print("10: Visualization")
print(Border)

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
sns.heatmap(confusion_matrix(Y_test, y_pred_lr),annot=True,cmap='Blues')
plt.title("Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.subplot(1,3,2)
sns.heatmap(confusion_matrix(Y_test, y_pred_dt),annot=True,cmap='Greens')
plt.title("Decision Tree")
plt.xlabel("Predicted")

plt.subplot(1,3,3)
sns.heatmap(confusion_matrix(Y_test, y_pred_knn),annot=True,cmap='Oranges')
plt.title("KNN")
plt.xlabel("Predicted")
plt.tight_layout()
plt.show()

#-------------------------------------------------------------
# Step 11: Final Result 
#-------------------------------------------------------------
print(Border)
print("11: Final Result")
print(Border)

Result = pd.DataFrame({
                    'Actual' : Y_test,
                    'Logistic':y_pred_lr,
                    'DecisionTree':y_pred_dt,
                    'KNN': y_pred_knn
                    })

print(" Final test result for patients on test data")
print(border1)
print(Result.head(20))

#-------------------------------------------------------------
# Step 12: Preserve Model in CSV
#-------------------------------------------------------------
print(Border)
print("12: Preserve Model in CSV")
print(Border)

Result.to_csv("DiabeticCaseStudyResult.csv")
print("Result of case study preserved in file")