class Country:
    def __init__(self):
        import pandas
        self.countries = pandas.read_csv("countries.csv")
        self.countries = self.countries[["Country", "Longitude", "Latitude"]]

    def getCountryLatLongPoints(self):
        return self.countries.set_index("Country").T.to_dict()
