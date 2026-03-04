import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40

############################################################
# step1:Load the Data set
############################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset loaded successfully")
print("First 5 entries from dataset")
print(df.head())

print("Last 5 entries from dataset")
print(df.tail())

############################################################
# step2:Data analysis
############################################################

print(Border)
print("Step 2: Data Analysis")
print(Border)

print("Number of Rows and Column in Dataset",df.shape)

print("Column in Dataset :",list(df.columns))

print("Datatype of columns :\n",df.dtypes)

print("Total Number of Student in Dataset ",df.shape[0])

print("Count of Passed student",df[df["FinalResult"]==1].shape[0])

print("Count of Failed student",df[df["FinalResult"]==0].shape[0])

print("Average study hours of students",df["StudyHours"].mean())

print("Average attendence of students ",df["Attendance"].mean())

print("Maximum previous score : ",df["PreviousScore"].max())

print("Minimum Sleep Hours :",df["SleepHours"].min())

result_counts = df["FinalResult"].value_counts()
print("Distribution of FinalResult:\n", result_counts)

total_students = df.shape[0]

pass_percentage = (result_counts[1] / total_students) * 100
fail_percentage = (result_counts[0] / total_students) * 100

print("Pass Percentage:", pass_percentage)
print("Fail Percentage:", fail_percentage)

############################################################
# step3 : Dataset Visualization 
############################################################

print(Border)
print("Step 3: Dataset visualization")
print(Border)

#Histogram representation for Study hours
sns.histplot(x=df["StudyHours"])
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()

# Scattor plot to display result according to study hours and sleeping time
passed = df[df["FinalResult"] == 1]
failed = df[df["FinalResult"] == 0]
sns.scatterplot(x=passed["StudyHours"], y=passed["PreviousScore"], label="Passed")
sns.scatterplot(x=failed["StudyHours"], y=failed["PreviousScore"], label="Failed")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("StudyHours vs PreviousScore")
plt.legend()
plt.show()

# Display attendance of students using boxplot
sns.boxplot(x=df["Attendance"])
plt.title("Boxplot of Attendance")
plt.xlabel("Attendance")
plt.show()

# Display result wrt assignment completed and final result
sns.boxplot(x=df["FinalResult"], y=df["AssignmentsCompleted"])
plt.title("Assignments Completed vs Final Result")
plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Assignments Completed")
plt.show()

# plot final result according to sleeping hours
sns.boxplot(x=df["FinalResult"], y=df["SleepHours"])
plt.title("Sleep Hours vs Final Result")
plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Sleep Hours")
plt.show()

############################################################
# Step 4 : Decide Independent and Dependent Variables
############################################################

print(Border)
print("Step 4 : Decide Independent and Dependent Variables ")
print(Border)

Feature_col=[
            "StudyHours",
            "Attendance",	
            "PreviousScore"	,
            "AssignmentsCompleted",
            "SleepHours"
            ]
X=df[Feature_col]
Y=df["FinalResult"]

print(" X shape : ",X.shape)
print(" Y Shape : ",Y.shape)

############################################################
# Step 5 : Split the Dataset for training and testing
############################################################

print(Border)
print("Step 5 : Split the Dataset for training and testing ")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size= 0.2,
    #random_state= 0 # Testing accuracy 83.333,Training 100
    #random_state=10 #Testing accuracy 83.333,Training 100
    random_state=42
)

print("X - Independent : ",X.shape)
print("Y - Dependent : ",Y.shape)

print("Data spliting activity done ")

print("X_train : ",X_train.shape) 

print("X_test : ",X_test.shape)  


print("Y_train : ",Y_train.shape) 
print("Y_test : ",Y_test.shape) 



############################################################
# Step 6 : Build the Model
############################################################

print(Border)
print("Step 6 : Build the Model ")
print(Border)


Model= DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,    #depth 5=100 /1 =100
    random_state=42
)

print("Model successfully created",Model)

############################################################
# Step 7 : Train the Model
############################################################

print(Border)
print("Step 7 : Train the Model ")
print(Border)

Model.fit(X_train,Y_train)

print("Model training completed")

############################################################
# Step 8 : Evaluate the Model
############################################################

print(Border)
print("Step 8 : Evaluate the Model ")
print(Border)

Y_pred=Model.predict(X_test)
Y_pred_training=Model.predict(X_train)
print(Y_pred.shape)

print("Expected Answers : ")
print(Y_test)

print("Predicted Answers: ")
print(Y_pred)

############################################################
# Step 8 : Evaluate the Model performance
############################################################
print(Border)
print("Step 9 : Evaluate the Model Performance ")
print(Border)

# acccuracy score
acccuracy=accuracy_score(Y_test,Y_pred)
print("Accuracy of model is : ",acccuracy*100)

#Confusion Matrix

Confusion_Matrix=confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix :\n ",Confusion_Matrix)


############################################################
# Calculate Training & Testing accuracy and predict model fitting
############################################################
Y_pred_training=Model.predict(X_train)
Training_acccuracy=accuracy_score(Y_train,Y_pred_training)
print("Training Accuracy of model is : ",Training_acccuracy*100)
print("Testing Accuracy of model is : ",acccuracy*100)

############################################################
# display feature importance 
############################################################

Importance =Model.feature_importances_
importance_df = pd.DataFrame({"Feature":Feature_col,"Importance":Importance}).sort_values(by="Importance",ascending=False)
print(importance_df)

############################################################
# Trained model by removing sleeping hours and compare accuracy
############################################################

Feature_col_2=[
            "StudyHours",
            "Attendance",	
            "PreviousScore"	,
            "AssignmentsCompleted"
            ]
X1=df[Feature_col]

X_train_2, X_test_2, Y_train_2, Y_test_2 = train_test_split(
    X1,
    Y,
    test_size= 0.2,
    random_state= 42
)

Model.fit(X_train_2,Y_train_2)
Y_pred_2=Model.predict(X_test_2)

acccuracy_2=accuracy_score(Y_test_2,Y_pred_2)
print("Accuracy of model after removing sleeping hours is : ",acccuracy_2*100)

if(acccuracy == acccuracy_2):
    print("Sleeping Hours not impacted on model acuuracy")

############################################################
# Trained model by removing sleeping hours and compare accuracy
############################################################

X2 = df[[Feature_col_2[0], Feature_col_2[1]]] 
X_train_X, X_test_X, Y_train_Y, Y_test_Y = train_test_split(
    X2,
    Y,
    test_size= 0.2,
    random_state= 42
)
Model.fit(X_train_X,Y_train_Y)
Y_pred_Y=Model.predict(X_test_X)
acccuracy_2=accuracy_score(Y_test_Y,Y_pred_Y)
print("Accuracy of model with Attendence and study hours : ",acccuracy_2*100)

############################################################
# Trained model by removing sleeping hours and compare accuracy
############################################################

ModelX= DecisionTreeClassifier(
    criterion="gini",
    max_depth=None,    #depth 5=100 /1 =100
    random_state=42
)
new_students = pd.DataFrame({
    "StudyHours": [10, 8, 6, 9, 7],
    "Attendance": [90, 85, 70, 95, 80],
    "PreviousScore": [75, 60, 50, 80, 65],
    "AssignmentsCompleted": [8, 7, 5, 9, 6],
    "SleepHours": [7, 6, 5, 8, 6]   # new feature
})
ModelX.fit(X_train,Y_train)
predictions = ModelX.predict(new_students)
new_students["PredictedResult"] = predictions

print(new_students)


for i, pred in enumerate(predictions):
    result = "Pass" if pred == 1 else "Fail"
    print(f"Student {i+1}: {result}")

misclassified = (Y_test.values != Y_pred)

print("Misclassified count:", sum(misclassified))
print(X_test[misclassified])

############################################################
# Decision Tree visualization
############################################################

plt.figure(figsize=(10,8))  # root note is study hours
plot_tree(
    Model,
    feature_names=X.columns,
    class_names=["Fail", "Pass"],
    filled=True
    )

plt.title("Decision Tree Visualization")
plt.show()


df["performanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]
X_new = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X_new, Y, test_size=0.2, random_state=42)

model_new = DecisionTreeClassifier()
model_new.fit(X_train, Y_train)

y_pred_new = model_new.predict(X_test)


acc_old = accuracy_score(Y_test, Y_pred)
acc_new = accuracy_score(Y_test, y_pred_new)

print("Old Accuracy:", acc_old)
print("New Accuracy:", acc_new)

model_full = DecisionTreeClassifier(max_depth=None)
model_full.fit(X_train, Y_train)

train_pred = model_full.predict(X_train)
train_acc = accuracy_score(Y_train, train_pred)

print("Training Accuracy:", train_acc)

test_pred = model_full.predict(X_test)
test_acc = accuracy_score(Y_test, test_pred)

print("Testing Accuracy:", test_acc)