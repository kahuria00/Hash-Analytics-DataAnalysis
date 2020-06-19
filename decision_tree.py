import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


iris_dataset=pd.read_csv('iris.csv')

#dividing the dataset into dependent and independent variables
X=iris_dataset.iloc[:,:-1].values #feature variable
Y=iris_dataset.iloc[:,4].values #Target

#Splitting Data
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=1)

# create decision tree object and Train Decision Tree Classifer
classifier=DecisionTreeClassifier()
classifier=classifier.fit(X_train,Y_train)
Y_predict=classifier.predict(X_test)

print(Y_predict)

#model Accuraccy
d=metrics.accuracy_score(Y_test, Y_predict)
print(d)

#accuracy 0.9555555555555556