import re
all_users={}
user_details={}
logged_user={}

# classs for handling user data
class Users(object):

    # method to add new user
    def add_user(self,email,names,password,role):

        if not self.validate_email(email):
            return {"message":"Please enter a valid email address"}
        if email in all_users:
            return  {"message":"Email already registered"}
        user_details['names']=names
        if not self.validate_password(password):
            return {"message":"Password does not meet the strength criteria"}
        user_details['password']=password
        user_details['role']=role

        all_users[email] = user_details

        return {'message':"user account succesfully created"}



    # method for user login
    def user_login(self,email,password):

        logged_user["email"]=email
        logged_user["password"]=password

        return {'message':"logged in"}





    # method to get all users
    def get_all_users(self):
        return all_users



    # method to get one user
    def get_one_user(self,email):

        if email in all_users:
            return all_users[email]

        return {'message':"user does not exist"}


    def validate_password(self,password):
        while True:
            if (len(password)<6 or len(password)>12):
                break
            elif not re.search("[a-z]",password):
                break
            elif not re.search("[A-Z]",password):
                break
            elif not re.search("[0-9]",password):
                break
            elif not re.search("[$#@]",password):
                break
            else:
                return password

    def validate_email(self,email):
        if re.match("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$)",email,re.IGNORECASE):
            return True
        return False
