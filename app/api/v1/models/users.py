import re
all_users={}
user_details={}
logged_user={}

# classs for handling user data
class Users(object):
    """
    This class has methods for manipulation of user data.
    """

    # method to add new user
    def add_user(self,email,names,password,role):
        """"
        This method adds anew user
        param1:email
        param2:names.
        paeram3:password.
        param4:role.

        returns: user added messages.
        raises:invalid email message.
        raises:email alrleady added message.
        raises:invalid role message.
        raises:week password error.


        """

        if not self.validate_email(email):
            return {"message":"Please enter a valid email address"}
        if email in all_users:
            return  {"message":"Email already registered"}
        user_details['names']=names
        if not self.validate_password(password):
            return {"message":"Password does not meet the strength criteria"}
        user_details['password']=password
        if not (role=="Admin" or role =="attendant"):

            return {'message':"Roles can only be admin and store attendant"}
        user_details['role']=role

        all_users[email] = user_details

        return {'message':"user account succesfully created"}



    # method for user login
    def user_login(self,email,password):
        """
        This method logs in a new user.
        param:email.
        param:password.
        returns:logged in message.
        """

        logged_user["email"]=email
        logged_user["password"]=password

        return {'message':"logged in"}






    # method to get all users
    def get_all_users(self):
        """
        This method gets all details users
        returns:all_users
        """
        return all_users



    # method to get one user
    def get_one_user(self,email):
        """
        This method gets one users details.
        returns:all_users
        """

        if email in all_users:
            return all_users[email]

        return {'message':"user does not exist"}


    def validate_password(self,password):
        """
        This method checks for strength of a password
        return:password
        """
        is_password_valid = True
        if (len(password)<6 or len(password)>12):
            is_password_valid = False
        elif not re.search("[a-z]",password):
            is_password_valid = False
        elif not re.search("[A-Z]",password):
            is_password_valid = False
        elif not re.search("[0-9]",password):
            is_password_valid = False
        elif not re.search("[$#@]",password):
            is_password_valid = False
        return is_password_valid



    def validate_email(self,email):
        if re.match("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$)",email,re.IGNORECASE):
            return True
        return False
