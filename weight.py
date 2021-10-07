import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

def lift_prediction(bw):
    data = pd.read_csv('/Users/Francis/Desktop/machinelearning/weightlifting.csv')
    data = data.drop_duplicates()
    data = data.dropna()
    #Changing the column names to lower case
    data.columns = [ x.lower().strip() for x in data.columns]

    data = data[['bodyweight', 'total']]
    data = data[data.total > 5]
    data = data[data.bodyweight > 5]
    data['bodyweight'] = data['bodyweight'] * 2.205
    data['total'] = data['total'] * 2.205
    
    X = data[['bodyweight']]
    Y = data[['total']]
    
    model = LinearRegression()
    model.fit(X,Y)

    X_test = np.array(bw)
    X_test = X_test.reshape((1,-1))


    return model.predict(X_test)[0]

