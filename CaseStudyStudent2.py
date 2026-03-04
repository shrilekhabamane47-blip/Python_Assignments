import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

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

sns.histplot(x=df["StudyHours"])
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()

passed = df[df["FinalResult"] == 1]
failed = df[df["FinalResult"] == 0]
sns.scatterplot(x=passed["StudyHours"], y=passed["PreviousScore"], label="Passed")
sns.scatterplot(x=failed["StudyHours"], y=failed["PreviousScore"], label="Failed")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("StudyHours vs PreviousScore")
plt.legend()
plt.show()

sns.boxplot(x=df["Attendance"])
plt.title("Boxplot of Attendance")
plt.xlabel("Attendance")
plt.show()

sns.boxplot(x=df["FinalResult"], y=df["AssignmentsCompleted"])
plt.title("Assignments Completed vs Final Result")
plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Assignments Completed")
plt.show()

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
    random_state= 42
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
    max_depth=None,    #depth 5=100 /1 =100
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

#Training Accuracy

Y_pred_training=Model.predict(X_train)
Training_acccuracy=accuracy_score(Y_train,Y_pred_training)
print("Training Accuracy of model is : ",Training_acccuracy*100)
print("Testing Accuracy of model is : ",acccuracy*100)

############################################################
# Step 8 : Evaluate New data
############################################################
#Predict the result for a student with the following 
print(Border)
print("Predict model for new student data ")
print(Border)

new_student = pd.DataFrame([[6, 85, 66, 7, 7]], columns=Feature_col)
result = Model.predict(new_student)

if result[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")

print(Border)