import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from math import floor


class Regression():
    def train(self, y_train, x_train):
        self.regr = linear_model.LinearRegression()

        self.regr.fit(y_train, x_train)

    def setTrainTestSet(self, x, y):
        ratio = 90
        length = len(x)
        trainlength = floor(len(x) * (ratio / 100))
        testlength = length - trainlength
        x_train = x[:-testlength]
        y_train = y[:-testlength]
        x_test = x[trainlength:]
        y_test = y[trainlength:]
        return x_train, y_train, x_test, y_test

    # Get the predicted value only
    def predict(self, year):
        dataframe = pd.DataFrame([year], columns=[''])
        pred = self.regr.predict(dataframe)
        return pred[0][0]

    # Get the predicted value raw value
    def errorPredict(self, df):
        return self.regr.predict(df)

    def getMAE(self, test, predicted):
        return mean_absolute_error(test, predicted)

    def getMSE(self, test, predicted):
        return mean_squared_error(test, predicted)
