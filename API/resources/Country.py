from flask_restful import Resource
from flask import request
from models.Country import Country as Model
from flask_jwt_simple import jwt_required

class Country(Resource):
    """ 
    Original get request endpoint commented out for debugging.
    @jwt_required
    # Authorization header, with value of: Bearer $accessKeyGoesHere$
    def get(self, countryName: str = None):
        # No mongoengine available for serializing mongoengine objects to json, so a manual way to do it:
        if(countryName is None):
            return self.parseMongoEngineObjectToJSON(Model.objects()), 200
        else:
            return self.parseMongoEngineObjectToJSON(Model.objects(countryName=countryName)), 200 
    """

    def get(self, countryName: str = None, year: int = None):
        from resources.Countries import Country
        longLatObj = Country()
        return longLatObj.getCountryLatLongPoints(), 200
            
    @jwt_required
    # Authorization header, with value of: Bearer $accessKeyGoesHere$
    def delete(self, countryName: str):
        modelObject = Model.objects(countryName=countryName)
        modelObject.delete()
        return {
            "message": "Successfully deleted " + countryName
        }, 204

    @jwt_required
    # Authorization header, with value of: Bearer $accessKeyGoesHere$
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
        
        return {
            "message" : "Successfully created country.",
            "href": "/countries/"+request.form.get("countryName")
        }, 201

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
