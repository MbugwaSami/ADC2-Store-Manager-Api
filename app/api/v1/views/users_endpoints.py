from flask import Flask, jsonify, request
from flask_restful import Resource

from ..models.users import Users, all_users


user_object=Users()
# endpoin for creating user

class UsersApi(Resource):

    def post(self):
        data=request.get_json()

        email = data.get('email')
        names = data.get('names')
        password = data.get('password')
        role = data.get('role')

        response = jsonify(user_object.add_user(email,names,password,role))

        response.status_code = 201

        return response

    def get(self):

        users = user_object.get_all_users()

        response = jsonify({"users":users,"message":"This are the users in the system"})


        response.status_code = 200


        return response

class SingleUserApi(Resource):

    def get(self,email):


         single_user = user_object.get_one_user(email)
         response = jsonify({"user":single_user,"message":"The above user was found"})
         response.status_code=200

         return response

    def post(self):

        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        response = jsonify({"user":user_object.user_login(email,password),"message":"logged in"})
        response.status_code =201
