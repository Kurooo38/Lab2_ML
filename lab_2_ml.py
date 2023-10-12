import numpy as np
import matplotlib.pyplot as mp
import pandas as pd
import streamlit as st


# Importing the dataset
dataset = pd.read_csv(r"User_Data.csv")
x = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,4].values
print(x[:10])
print(x.shape)
print(y.shape)
fig = mp.figure()

st.title('Dataset :')
st.write(dataset.head())

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.25, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(x_test)
print(y_pred)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Visualising the Training set results
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
fig, ax = mp.subplots()
ax.scatter([1, 2, 3], [1, 2, 3])
X1, X2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
mp.contourf(X1,X2, classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
            alpha = 0.75, cmap = ListedColormap(('red','green')))
mp.xlim(X1.min(), X1.max())
mp.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
  mp.scatter(x_set[y_set == j, 0],x_set[y_set == j, 1],
             c = ListedColormap(('red', 'green'))(i),label = j)
mp.title('Naive Bayes (Training set)')
mp.xlabel('Age')
mp.ylabel('Estimated Salary')
mp.legend()
st.header('Training set :')
st.pyplot(fig)

# Visualising the Test set results
from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
fig2, ax2 = mp.subplots()
ax2.scatter([1, 2, 3], [1, 2, 3])
X1, X2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
mp.contourf(X1,X2, classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
            alpha = 0.75, cmap = ListedColormap(('purple','green')))
mp.xlim(X1.min(), X1.max())
mp.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
  mp.scatter(x_set[y_set == j, 0],x_set[y_set == j, 1],
             c = ListedColormap(('purple', 'green'))(i),label = j)
mp.title('Naive Bayes (Test set)')
mp.xlabel('Age')
mp.ylabel('Estimated Salary')
mp.legend()
st.header('Test set :')
st.pyplot(fig2)
