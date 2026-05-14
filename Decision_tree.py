# Predicting Exam Results Using Decision Tree

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Create dataset manually (at least 10 records)
data = {
    "Preparation_Time": [2, 5, 1, 4, 3, 6, 2, 5, 1, 4],
    "Assignment_Submission": [
        "OnTime", "OnTime", "Late", "OnTime", "Late",
        "OnTime", "Late", "OnTime", "Late", "OnTime"
    ],
    "Final_Result": [
        "Pass", "Pass", "Fail", "Pass", "Fail",
        "Pass", "Fail", "Pass", "Fail", "Pass"
    ]
}

df = pd.DataFrame(data)

# 2. Convert Final_Result into numeric values
df["Final_Result"] = df["Final_Result"].map({"Pass": 1, "Fail": 0})

# Convert Assignment_Submission into numeric
df["Assignment_Submission"] = df["Assignment_Submission"].map({"OnTime": 1, "Late": 0})

# Features (X) and Target (y)
X = df[["Preparation_Time", "Assignment_Submission"]]
y = df["Final_Result"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3. Train Decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)

# 4. Calculate and display accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)