from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_diabetes

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