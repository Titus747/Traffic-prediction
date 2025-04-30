"""import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\user\\Downloads\\Traffic.csv")
print(df)
print(df.shape)
print(df.columns)
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
df.drop(["Time"],axis=1,inplace=True)
print(df)

c=LabelEncoder()
df["Day of the week"]=c.fit_transform(df["Day of the week"])
df["Traffic Situation"]=c.fit_transform(df["Traffic Situation"])
print(df)

x = df.drop(columns=["Traffic Situation"])
y = df["Traffic Situation"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(len(x_train))
print(len(y_train))

model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy:{:.2f}%".format(accuracy * 100))
print("confusion matrix:\n",confusion_matrix(y_test,y_pred))
print("\nclassification report:\n",classification_report(y_test,y_pred))
print(df.describe())
print(df.corr())
plt.figure(figsize=(10,10))
sns.heatmap(df.corr())
plt.show()"""

