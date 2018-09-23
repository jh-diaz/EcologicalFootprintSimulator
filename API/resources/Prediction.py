from flask_restful import Resource
from flask import request

class Prediction(Resource):
    def get(self, countryName, year):
        from ml.Footprint import Footprint as Prediction
        try:
            model = Prediction()
            footprintPrediction = model.getFootprints(countryName, year)
            populationPrediction = model.getPopulation(countryName, year)
            print(footprintPrediction)
            print(populationPrediction)
            return {
                "Country" : countryName,
                "Population": populationPrediction[0],
                "Year": year,
                "Cropland Footprint" : footprintPrediction[0][1],
                "Grazing Footprint" : footprintPrediction[1][1],
                "Forest Footprint" : footprintPrediction[2][1],
                "Carbon Footprint" : footprintPrediction[3][1],
                "Fish Footprint" : footprintPrediction[4][1]
            }, 200
        except:
            return{
                "Message": "Erroneous response from the server. Country might not be supported."
            }, 404

