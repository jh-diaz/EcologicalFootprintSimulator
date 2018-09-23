class Country:
    def __init__(self):
        import pandas
        self.countries = pandas.read_csv("countries.csv")
        self.countries.drop(self.countries.columns[[0]], axis=1, inplace=True)

    def getCountryLatLongPoints(self):
        return self.countries.set_index("Country").T.to_dict()