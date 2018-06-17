# Simple Linear Regression

# from sklearn.model_selection import train_test_split

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, 0]
Y = dataset.iloc[:, 1]