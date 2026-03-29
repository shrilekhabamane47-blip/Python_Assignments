import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns


Border = "="*100
border1 = "-"*100

#---------------------------------------------------------------
# Step 1 : Load the dataset
#---------------------------------------------------------------
print(Border)
print("Step 1 : Load the dataset")
print(Border)

df = pd.read_csv("bank-full.csv",sep=';')   
print("Shape of dataset:", df.shape)
print(border1)
print("First Five records:")
print(df.head())

#---------------------------------------------------------------
# Step 2 : Data Analysis
#---------------------------------------------------------------
print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Info:")
print(df.info())
print(border1)
print("Missing values count:")
print(df.isnull().sum())
print(border1)
print("Statistical report:")
print(df.describe())
print("Unknown values")
print(df.isin(['unknown']).sum())

for col in ['job','education']:
    mode_val = df[df[col]!='unknown'][col].mode()[0]
    mode_val= df[col].mode()[0]
    df[col]=df[col].replace('unknown',mode_val)

print(df.head(10))

#---------------------------------------------------------------
# Step 3 : Data Visualization
#---------------------------------------------------------------
print(Border)
print("Step 3 : Data Visualization")
print(Border)

plt.figure(figsize=(8,5))
sns.countplot(x="y", data=df)
plt.title("class Distribution of dependent variable")
plt.show()

#---------------------------------------------------------------
# Step 4 : Data Preprocessing
#---------------------------------------------------------------
print(Border)
print("Step 4 : Data Preprocessing")
print(Border)

categorical_cols = ["job","marital","education","default","housing","loan","contact","month","poutcome","y"]

for col in categorical_cols:
    df[col] = LabelEncoder().fit_transform(df[col])
print(df.head())


numeric_cols = ["age","balance","day","duration","campaign","pdays","previous"]

scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("Numeric features scaled successfully")
print(df.head())

#---------------------------------------------------------------
#Step 5: Split the dataset for training and testing
#---------------------------------------------------------------
print(Border)
print("Step 5: Split the dataset for training and testing")
print(Border)

X = df.drop("y", axis=1)  
y = df["y"]               

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42, stratify=y)

print("Shape of Training Features:", X_train.shape)
print("Shape of Testing Features:", X_test.shape)
print("Shape of Training Labels:", y_train.shape)
print("Shape of Testing Labels:", y_test.shape)

#----------------------------------------------------------
#Step 6 : Create Classification Models
#----------------------------------------------------------
print(Border)
print("Step 6 : Create Classification Models")
print(Border)

model_lr  = LogisticRegression(max_iter=5000, random_state=42)
model_knn = KNeighborsClassifier(n_neighbors=5)
model_rf  = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1)

#----------------------------------------------------------
#Step 7 : Train Classification models
#----------------------------------------------------------
print(Border)
print("Step 7 : Train Classification Models")
print(Border)
model_lr.fit(X_train, y_train)
model_knn.fit(X_train, y_train)
model_rf.fit(X_train, y_train)
print("Models trained successfully")
#-------------------------------------------------------------
# Step 8: Test Classification model
#-------------------------------------------------------------

print(Border)
print("Step 8 : Test Classification models")
print(Border)
y_pred_lr  = model_lr.predict(X_test)
y_pred_knn = model_knn.predict(X_test)
y_pred_rf  = model_rf.predict(X_test)
print("Models Test successfully")

#-------------------------------------------------------------
# Step 9: Evaluate  model
#-------------------------------------------------------------
print(Border)
print("Step 9: Evaluate  model Performance")
print(Border)
acc_lr  = accuracy_score(y_test, y_pred_lr)*100
acc_knn = accuracy_score(y_test, y_pred_knn)*100
acc_rf  = accuracy_score(y_test, y_pred_rf)*100

print("------------Accuracy Score of models-------------------")
print(border1)
print("Logistic Regression Accuracy    : ",acc_lr)
print("K-Nearest neighbors Accuracy    : ",acc_knn)
print("Random Forest classfier Accuracy: ",acc_rf)

print(border1)
print("------------Confusion matrix of models-------------------")
print(border1)
print("Confusion Matrix Logistic Regression:\n", confusion_matrix(y_test, y_pred_lr))
print("Confusion Matrix KNN classifier:\n", confusion_matrix(y_test, y_pred_knn))
print("Confusion Matrix Random Forest:\n", confusion_matrix(y_test, y_pred_rf))

print(border1)
print("------------Classification Report of models------------------")
print(border1)

print("Logistic Regression:")
print(classification_report(y_test, y_pred_lr))
print(border1)

print("KNN classifier:")
print(classification_report(y_test, y_pred_knn))
print(border1)

print("Random Forest:")
print(classification_report(y_test, y_pred_rf))
print(border1)

print("------------ROC AUC Curve------------------")
print(border1)

Prob_LR = model_lr.predict_proba(X_test)[:,1]
ROC_AUC_LR = roc_auc_score(y_test,Prob_LR)*100
print("Logistic Regression ROC AUC Score:", ROC_AUC_LR)
print(border1)

Prob_KNN = model_knn.predict_proba(X_test)[:,1]
ROC_AUC_KNN = roc_auc_score(y_test,Prob_KNN)*100
print("KNN classifier ROC AUC Score:", ROC_AUC_KNN)
print(border1)

Prob_RF = model_rf.predict_proba(X_test)[:,1]
ROC_AUC_RF = roc_auc_score(y_test,Prob_RF)*100
print("Random Forest ROC AUC Score:", ROC_AUC_RF)
print(border1)

#-------------------------------------------------------------
# Step 10: Visualization
#-------------------------------------------------------------
print(Border)
print("10: Visualization")
print(Border)

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
sns.heatmap(confusion_matrix(y_test, y_pred_lr),annot=True,fmt="d",cmap='Blues')
plt.title("Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.subplot(1,3,2)
sns.heatmap(confusion_matrix(y_test, y_pred_knn),annot=True,fmt="d",cmap='Oranges')
plt.title("KNN")
plt.xlabel("Predicted")


plt.subplot(1,3,3)
sns.heatmap(confusion_matrix(y_test, y_pred_rf),annot=True,fmt="d",cmap='Greens')
plt.title("Random forest")
plt.xlabel("Predicted")
plt.tight_layout()
plt.show()



fpr_lr, tpr_lr, _ = roc_curve(y_test, Prob_LR)
fpr_knn, tpr_knn, _ = roc_curve(y_test, Prob_KNN)
fpr_rf, tpr_rf, _ = roc_curve(y_test, Prob_RF)


plt.figure(figsize=(8,6))
plt.plot(fpr_lr, tpr_lr, label=f"Logistic Regression (AUC = {ROC_AUC_LR:.2f})", color="blue")
plt.plot(fpr_knn, tpr_knn, label=f"KNN (AUC = {ROC_AUC_KNN:.2f})", color="green")
plt.plot(fpr_rf, tpr_rf, label=f"Random Forest (AUC = {ROC_AUC_RF:.2f})", color="orange")
plt.plot([0,1],[0,1], color="red", linestyle="--")

plt.title("ROC Curves for Logistic Regression, KNN, and Random Forest")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend(loc="lower right")
plt.show()