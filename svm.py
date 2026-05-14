import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
 
Data = {
        "Experience":[1,2,3,4,5,6,7,8,9,10],
        "Qualification":[1,1,1,2,2,2,1,2,1,2], 
        "Income":[0,0,0,1,1,1,0,1,0,1] 
}
df = pd.DataFrame(Data) 
print(df)


X = df[["Experience","Qualification"]]
y = df["Income"]


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3) 
Model = SVC(kernel="linear") 
Model.fit(X_train,y_train) 


Prediction = Model.predict(X_test) 
Accuracy = accuracy_score(y_test,Prediction) 
print("Accuracy",Accuracy)