from flask import Flask
from flask_restful import Api
from DatabaseConnection import DatabaseConnection
from resources.Country import Country
from resources.User import User
from flask_jwt_simple import JWTManager, jwt_required
import secrets

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = secrets.token_hex(nbytes=16)
jwtAuthentication = JWTManager(app)

api = Api(app)

dbConnection = DatabaseConnection("ecofootprint", "mongodb://Joshua:12345@localhost/ecofootprint")

api.add_resource(Country, "/countries", "/countries/", "/countries/<string:countryName>")
api.add_resource(User, "/auth")

app.run(debug=True)