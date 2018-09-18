import pandas as pd
import LinearRegression as lr


class Footprint:
    def __init__(self):
        self.df = pd.read_csv('compiled data.csv')
        self.footprints = ['Cropland Footprint', 'Grazing Footprint', 'Forest Footprint', 'Carbon Footprint',
                           'Fish Footprint']

    def getPopulation(self, country, year):
        y = (self.df[self.df['Country'] == country])

        self.checkIfCountryExists(y)

        # get years
        years = []
        for i in range(2000, 2016):
            years.append(i)
        yearValues = []
        for i in years:
            yearValues.append(y[str(i)].tolist())
        for i in range(len(years)):
            yearValues[i].insert(0, years[i])
        df = pd.DataFrame(yearValues, columns=['year', 'yearValues'])
        x = df[['yearValues']]
        y = df[['year']]
        regression = lr.Regression()
        xr, yr, xt, yt = regression.setTrainTestSet(x, y)
        regression.train(yr, xr)
        ans = regression.errorPredict(yt)
        error = regression.getMAE(xt, ans)
        # print('mean abs error: %.2f' % regression.getMAE(xt, ans))

        pred = regression.predict(year)
        return pred, error

    def getFootprints(self, country, year):
        pop = self.getPopulation(country, 2016)
        row = (self.df[self.df['Country'] == country])
        self.checkIfCountryExists(row)
        footprintValues = []
        for i in self.footprints:
            footprintValues.append(row[str(i)].tolist())
        for i in range(len(self.footprints)):
            footprintValues[i].insert(0, self.footprints[i])
        return (footprintValues)

    def checkIfCountryExists(self, country):
        # IF NO COUNTRY EXIST IN CSV
        if len(country) == 0:
            raise ValueError('(%s) country is not found in the database.' % country)


f = Footprint()
print(f.getFootprints('Afghanistan', 2004))
