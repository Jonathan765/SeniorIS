from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_diabetes

'''
The file contains the two functions that load the Breast Cancer Wisconsin and Diabetes datasets
'''

def load_breast_cancer_data():
    data = load_breast_cancer()
    X = data.data
    y = data.target
    return X, y

def load_diabetes_data():
    data = load_diabetes()
    X = data.data
    y = data.target
    return X, y