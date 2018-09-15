from flask_restful import Resource
from models.Country import Country as Model

class Country(Resource):
    def get(self, countryName: str = None):
        countryDict = {}
        # No mongoengine available for serializing mongoengine objects to json, so a manual way to do it:
        if(countryName is None):
            for model in Model.objects():
                countryDict[model.countryName] = {
                    "population" : model.population,
                    "cropland" : model.cropland,
                    "grazing" : model.grazing,
                    "forest" : model.forest,
                    "carbon" : model.carbon,
                    "fish" : model.fish,
                    "earthsRequired" : model.earthsRequired
                }
        else:
            model = Model.objects(countryName=countryName)[0]
            countryDict[countryName] = {
                    "population" : model.population,
                    "cropland" : model.cropland,
                    "grazing" : model.grazing,
                    "forest" : model.forest,
                    "carbon" : model.carbon,
                    "fish" : model.fish,
                    "earthsRequired" : model.earthsRequired
            }
        return countryDict, 200
