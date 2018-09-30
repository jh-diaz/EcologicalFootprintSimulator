from flask_restful import Resource
from flask import request

class Graph(Resource):
    def get(self, countryName):
        from ml.Footprint import Footprint as Prediction
        try:
            model = Prediction()
            output = {}
            for year in range(2000, 2021):
                footprintPrediction = model.getFootprints(countryName, year)
                populationPrediction = model.getPopulation(countryName, year)
                output[year] = {
                    "Country": countryName,
                    "Population": populationPrediction[0],
                    "Cropland Footprint": footprintPrediction[0][1],
                    "Grazing Footprint": footprintPrediction[1][1],
                    "Forest Footprint": footprintPrediction[2][1],
                    "Carbon Footprint": footprintPrediction[3][1],
                    "Fish Footprint": footprintPrediction[4][1]
                }

            return output, 200
        except:
            return{
                "Message": "Erroneous response from the server. Country might not be supported."
            }, 404

