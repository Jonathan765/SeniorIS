import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from .linear import LinearModel

def train_logistic_linear_regression_model(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_scaled, y)

    return LinearModel(
        weights=clf.coef_[0],
        bias=clf.intercept_[0],
    )

def train_linear_regression_model(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    clf = LinearRegression()
    clf.fit(X_scaled, y)

    return LinearModel(
        weights=clf.coef_,
        bias=clf.intercept_,
    )
