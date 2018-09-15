from flask import Flask
from flask_restful import Api
from resources.Country import Country
from DatabaseConnection import DatabaseConnection

app = Flask(__name__)
api = Api(app)
dbConnection = DatabaseConnection("ecofootprint", "mongodb://Joshua:12345@localhost/ecofootprint")

api.add_resource(Country, "/countries", "/countries/" "/countries/<string:countryName>")
app.run(debug=True)