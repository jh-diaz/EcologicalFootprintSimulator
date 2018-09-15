from mongoengine import *

class Country(DynamicDocument):
    countryName = StringField(min_length=3, max_length=15)
    