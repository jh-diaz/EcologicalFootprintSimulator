import pandas as pd
import LinearRegression as lr


class Footprint:
    def __init__(self):
        self.df = pd.read_csv('compiled data.csv')
        self.footprints = ['Cropland Footprint', 'Grazing Footprint', 'Forest Footprint', 'Carbon Footprint',
                           'Fish Footprint']  # , 'Urban Land']

    # Gets the population (in millions)
    # input requires the country and the year you want the predicted population to be in
    def getPopulation(self, country, year):
        y = (self.df[self.df['Country'] == country])

        self.checkIfCountryExists(y)

        # get years
        years = []
        for i in range(2000, 2015):
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
        # print('mean sq error: %.2f' % regression.getMSE(xt, ans))

        pred = regression.predict(year)
        return pred, error

    # Gets the footprints (Cropland, Grazing, Forest, Carbon, Fish, Urban Land)
    # input requires the country and the year you want the predicted footprint to be in
    def getFootprints(self, country, year):
        pop = self.getPopulation(country, 2016)[0]
        pop2 = self.getPopulation(country, year)[0]
        popInc = pop2 - pop
        row = (self.df[self.df['Country'] == country])
        self.checkIfCountryExists(row)
        footprintValues = []
        yearValues = []
        for i in self.footprints:
            footprintValues.append(row[str(i)].tolist())
        for i in range(len(self.footprints)):
            footprintValues[i].insert(0, self.footprints[i])
        for i in footprintValues:
            resourceIncRatio = popInc * i[1]
            newFpValue = (resourceIncRatio + i[1]) * pop2
            yearValues.append([i[0], newFpValue])
        return yearValues

    def checkIfCountryExists(self, country):
        # IF NO COUNTRY EXIST IN CSV
        if len(country) == 0:
            raise ValueError('(%s) country is not found in the database.' % country)

# example usage
# f = Footprint()
# print(f.getPopulation('Afghanistan', 2014))
