# CS 1302 PROJECT: CLASSIFICATION MODEL
# by: ERIC HOANG, RYAN PHAM, & TAOFFEK ADEYANJU

import os
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_excel(os.path.join(os.path.dirname(__file__), 'Dry_Bean_Dataset.xlsx'))
x = data.iloc[:,:-1].values
y = data['Class']

# splitting into train & test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train)
knn_pred = knn.predict(x_test)
print(accuracy_score(knn_pred, y_test))
print(classification_report(knn_pred, y_test))