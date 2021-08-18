import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

def mark_predict(th,mil,tx,pg,engine):
    # import data
    data = pd.read_csv("ford.csv")


    # encoder data
    encode = preprocessing.LabelEncoder()

    encode.fit(data.transmission.drop_duplicates())
    data.transmission = encode.transform(data.transmission)

    encode.fit(data.fuelType.drop_duplicates())
    data.fuelType = encode.transform(data.fuelType)

    encode.fit(data.model.drop_duplicates())
    data.model = encode.transform(data.model)

    #Dropping data
    data.drop(columns=['fuelType','transmission'], inplace=True)

    #Pengurutan data
    nw_data = data[['model','year','mileage','tax','mpg','engineSize','price']]


    #feature and label selection
    x = nw_data.iloc[:, 1:6].values
    y = nw_data.iloc[:, -1].values

    #Split data --> Train and split

  
    #Building model Linear regression
    lr = LinearRegression()
    lr.fit(x, y)

    #Predict
    X_test = np.array([th,mil,tx,pg,engine])
    X_test = X_test.reshape((1,-1))
    pred = lr.predict(X_test)[0]


    return round(pred)


