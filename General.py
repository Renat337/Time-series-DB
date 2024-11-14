import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rn

path = pd.read_csv("SPX.csv")
path.Date = pd.to_datetime(path.Date)
ht,wd = path.shape

for i in range(ht):
    x=rn.random()
    path.loc[i,"Open"] = None if x<0.1 else path.loc[i,"Open"]

def missingvals(column):
    missing = path.loc[path[column].isnull()]
    if len(missing)/ht > 0.2:
        return "Too many missing to linearly extrapolate."

    # count=0
    # while missing.index[count]==count:
    #     count+=1
    # path.drop(columns=[count,wd])

    #using mean imputation
    for i in missing.index:
        count=1
        while i+count<ht and path[column][i+count]=="nan":
            count+=1
        if i+count>=ht:
            break
        l,r = i-1,i+count
        ldays, rdays = (path.Date[i]-path.Date[l]).days, (path.Date[r]-path.Date[i]).days
        path.loc[i,column]=(rdays*l+ldays*r)/(ldays+rdays)

def datacleaning():
    pass

def predict():
    pass

def plot(column, n=ht):
    plt.plot(path["Date"].tail(n),path[column].tail(n))
    plt.ylabel(column)