import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error
from math import floor


class Regression():
    def __init__(self, country, column):
        df = pd.read_csv('test.csv')

        df = (df[df['country'].str.contains(country)])

        x = df[[column]]
        y = df[['year']]

        x_train, y_train, x_test, y_test = self.setTrainTestSet(x, y)

        self.regr = linear_model.LinearRegression()

        self.regr.fit(y_train, x_train)

        y_pred = self.regr.predict(x_test)

        # print('coeff: ', self.regr.coef_)
        #
        # print('mean abs error: %.2f' % mean_absolute_error(y_test, y_pred))

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

    def predict(self, year):
        dataframe = pd.DataFrame([year], columns=[''])
        pred = self.regr.predict(dataframe)
        return pred[0][0]

