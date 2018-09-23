from flask import Flask
from flask_restful import Api
from DatabaseConnection import DatabaseConnection
from resources.Country import Country
from resources.User import User
from resources.Prediction import Prediction
from flask_jwt_simple import JWTManager, jwt_required
from flask_cors import CORS
import secrets

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = secrets.token_hex(nbytes=16)
jwtAuthentication = JWTManager(app)
CORS(app)

api = Api(app)

dbConnection = DatabaseConnection("ecofootprint", "mongodb://Joshua:12345@localhost/ecofootprint")

api.add_resource(Country, "/countries")
api.add_resource(User, "/auth")
api.add_resource(Prediction, "/predict/<string:countryName>/<string:year>")

app.run(debug=True)