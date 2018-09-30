class Country:
    def __init__(self):
        import pandas
        self.countries = pandas.read_csv("API/resources/countries.csv")

    def getCountryLatLongPoints(self):
        return self.countries.set_index("Country").T.to_dict()
    
    def getAverageMAE(self):
        from ml.Footprint import Footprint as Prediction
        self.countries = self.countries.set_index("Country").T.to_dict()
        totalCountries = 167
        sumMAE = 0
        model = Prediction()
        for key in self.countries.keys():
            sumMAE += model.getPopulation(key, 2000)[1]

        return sumMAE/totalCountries
