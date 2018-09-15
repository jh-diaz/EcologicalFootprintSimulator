from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp
from resources.AuthUsers import *
from flask_jwt_simple import create_jwt

class User(Resource):
    def post(self):
        if not request.is_json:
            return {
                "message": "Data should be in json format."
            }, 400

        data = request.get_json()
        username = data.get("username", None)
        password = data.get("password", None)

        if not username:
            return {
                "message" : "Invalid username."
            }, 400
            
        if not password:
            return {
                "message" : "Invalid password."
            }
        
        matchingUser = users.get(username, None)
        if matchingUser and safe_str_cmp(matchingUser["password"], password):
            return {
                "access_token" : create_jwt(identity=username)
            }, 200