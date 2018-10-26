from flask import Flask, jsonify, request
from flask_restful import Resource

from ..models.users import Users, all_users


user_object=Users()
# endpoin for creating user

class UsersApi(Resource):
    """
    This class has post and get method of all users.
    """

    def post(self):
        """"
        This method posts data of a user.
        returns: json response.



        """
        data=request.get_json()
        if not data:
            return {'message':'fields can not be empty'}

        email = data.get('email')
        names = data.get('names')
        password = data.get('password')
        role = data.get('role')
        if user_object.get_one_user(email):
            return  {"message":"Email already registered"}
        if not user_object.validate_email(email):
            return {"message":"Please enter a valid email address"}

        if not user_object.validate_password(password):
            return {"message":"Password does not meet the strength criteria"}

        response = jsonify(user_object.add_user(email,names,password,role))

        response.status_code = 201

        return response

    def get(self):
        """
        This method gets data of all users.
        returns:Details of a user.
        """

        users = user_object.get_all_users()

        response = jsonify({"users":users,"message":"This are the users in the system"})


        response.status_code = 200


        return response

class SingleUserApi(Resource):
    """
    This class has post and get methods for single user data.
    """

    def get(self,email):
         """
         This method gets data of a single user.
         returns:details of a single user
         """
         single_user = user_object.get_one_user(email)
         response = jsonify({"user":single_user,"message":"The above user was found"})
         response.status_code=200

         return response

    def post(self):
        """"
        This method posts data of a user login.


        """

        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        response = jsonify({"user":user_object.user_login(email,password),"message":"logged in"})
        response.status_code =201
