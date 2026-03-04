import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*40

############################################################
# Load the Data set
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
# Data analysis
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
# Dataset Visualization 
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