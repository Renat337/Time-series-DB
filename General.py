import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = pd.read_csv("SPX.csv")
path.Date = pd.to_datetime(path.Date)

def missingvals(column):
    pass

def datacleaning():
    pass

def predict():
    pass

def plot(column):
    plt.plot(path["Date"],path[column])
    plt.ylabel(column)
    plt.show()