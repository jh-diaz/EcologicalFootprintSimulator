from mongoengine import *

class Country(Document):
    ## Could've done this in one line, but for readability purposes..
    countryName = StringField(max_length=15)
    population = StringField(max_length=15)
    cropland = StringField(max_length=15)
    grazing = StringField(max_length=15)
    forest = StringField(max_length=15)
    carbon = StringField(max_length=15)
    fish = StringField(max_length=15)
    earthsRequired = StringField(max_length=15)