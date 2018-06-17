# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv(path)
X = dataset.iloc[:, 0]
y = dataset.iloc[:, 1]

# Splitting the dataset into training and test data
# Making test size 1/3rd of the data set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)