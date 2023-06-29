import pandas as pd
from sklearn.linear_model import LinearRegression

def make_model():
    data = pd.read_csv("plik.csv", sep="\ +", engine="python")
    data.columns = [
        "kolumna1",
        "kolumna2",
        "kolumna3"
    ]
    #split data
    X = data[[
        "kolumna1",
        "kolumna2"
    ]]
    y = data["kolumna3"]
    #Train model
    model = LinearRegression()
    model.fit(X, y)
    return model