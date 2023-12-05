from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

iris = pd.read_csv("IRIS.csv")

X = iris.iloc[:, :-1]
Y = iris.iloc[:, -1]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=6)

knn = KNeighborsClassifier(n_neighbors=6, weights='distance')
dt = DecisionTreeClassifier()
lr = LogisticRegression(solver='liblinear')

acc = {}

knn.fit(X_train, Y_train)
dt.fit(X_train, Y_train)
lr.fit(X_train, Y_train)

a, b, c = dt.score(X_test, Y_test), lr.score(X_test, Y_test), knn.score(X_test, Y_test)

acc = pd.DataFrame({'models': ['Decistiontree', 'LogisticRegression', 'KNN'], 'accuracy': [a, b, c]})

print(acc)