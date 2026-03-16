import pandas as pd

import joblib #to save trained model

from sklearn.preprocessing import LabelEncoder 
#sklearn- Scikit learn
#preprocessing- used for data preparation before training ML model
#LabelEncoder- tool used to convert text categories into number

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("train.csv")

print(df.info())
print(df.describe())
print(df.isnull().sum())

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender']) 
#fit_transform, learns all unique values and converts into number
df['Degree'] = le.fit_transform(df['Degree'])
df['Branch'] = le.fit_transform(df['Branch'])
df['Placement_Status'] = le.fit_transform(df['Placement_Status'])

df = df.drop("Student_ID", axis=1) 
#we are removng Student_ID column because its not helpful for placement
#axis=0 removes row and axis=1 removes column

print(df.head())

X = df.drop("Placement_Status", axis=1)
y = df["Placement_Status"]

print(X.head())
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
    # test_size=0.2 it is 20% of the data -> testing and 80% -> training
)

print(X_train.shape)
print(X_test.shape)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
# fit - trains the model
# X_train - training features (i/p variables used by model to make predictions)
# y_train - training labels (o/p the model is trained to predict)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_pred)
print("Decision Tree Accuracy:", dt_accuracy)

rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)
print("Random Forest Accuracy:", rf_accuracy)

knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)
knn_pred = knn_model.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_pred)
print("KNN Accuracy:", knn_accuracy)

print("\nLogistic Regression Report")
print(classification_report(y_test, y_pred))
print("\nDecision Tree Report")
print(classification_report(y_test, dt_pred))
print("\nRandom Forest Report")
print(classification_report(y_test, rf_pred))
print("\nKNN Report")
print(classification_report(y_test, knn_pred))

print(confusion_matrix(y_test, rf_pred))

joblib.dump(rf_model, "placement_model.pkl")