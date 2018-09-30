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
                "Population": round(populationPrediction[0]/1000000,1),
                "Year": year,
                "Cropland Footprint" : round(footprintPrediction[0][1],2),
                "Grazing Footprint" : round(footprintPrediction[1][1],2),
                "Forest Footprint" : round(footprintPrediction[2][1],2),
                "Carbon Footprint" : round(footprintPrediction[3][1],2),
                "Fish Footprint" : round(footprintPrediction[4][1],2),
                "Percentage of error" : round(populationPrediction[1]/10000,2)
            }, 200
        except Exception as x:
            print(x)
            return{
                "Message": "Erroneous response from the server. Country might not be supported."
            }, 404

