# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv("Salary_Data.csv")
X = dataset.iloc[:, 0:1]
y = dataset.iloc[:, -1]

# Splitting the dataset into training and test data
# Making test size 1/3rd of the data set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

# Fitting linear regression model to training set 
# (This library also does feature scaling)
from sklearn.linear_model import LinearRegression

# Least ordinary squares linear regression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the test set results
hypothesis_y = regressor.predict(X_test)

# Visualising the training set results

# Scatter plot of points
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

# Visualising the test set results

# Seeing how our model does on a new set of data
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_train, regressor.predict(X_train), color='red')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()