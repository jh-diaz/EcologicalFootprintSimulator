from flask_restful import Resource
from flask import request
from models.Country import Country as Model

class Country(Resource):
    def get(self, countryName: str = None):
        countryDict = {}
        # No mongoengine available for serializing mongoengine objects to json, so a manual way to do it:
        if(countryName is None):
            return self.parseMongoEngineObjectToJSON(Model.objects())
        else:
            return self.parseMongoEngineObjectToJSON(Model.objects(countryName=countryName))
    
    def delete(self, countryName: str):
        modelObject = Model.objects(countryName=countryName)
        modelObject.delete()
        return {"msg": "Successfully deleted " + countryName}, 200

    def post(self):
        newCountry = Model(countryName=request.form.get("countryName"), 
        population=request.form.get("population"),
        cropland=request.form.get("cropland"),
        grazing=request.form.get("grazing"),
        forest=request.form.get("forest"),
        carbon=request.form.get("carbon"),
        fish=request.form.get("fish"),
        earthsRequired=request.form.get("earthsRequired"))
        newCountry.save()
        
        return {"message" : "Successfully created country."}, 201

    def parseMongoEngineObjectToJSON(self, modelObjects):
        countryDict = {}
        for modelObject in modelObjects:
            countryDict[modelObject.countryName] = self.serializeCountry(modelObject)
        
        return countryDict

    def serializeCountry(self, modelObject):
        return {
            "population" : modelObject.population,
            "cropland" : modelObject.cropland,
            "grazing" : modelObject.grazing,
            "forest" : modelObject.forest,
            "carbon" : modelObject.carbon,
            "fish" : modelObject.fish,
            "earthsRequired" : modelObject.earthsRequired
        }
