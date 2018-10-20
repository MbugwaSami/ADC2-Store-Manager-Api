all_users={}
user_details={}
logged_user={}

# classs for handling user data
class Users(object):

    # method to add new user
    def add_user(self,email,names,password,role):

        if email in all_users:
            return  {"message":"Email already registered"}

        user_details['names']=names
        user_details['password']=password
        user_details['role']=role

        all_users[email] = user_details

        return {'message':"user account succesfully created"}



    # method for user login
    def user_login(self,email,password):
        
        logged_user["email"]=email
        logged_user["password"]=password

        return {'message':"logged in"}




    def get_user_email():
            pass    



    # method to get all users
    def get_all_users(self):
        return all_users



    # method to get one user
    def get_one_user(self,email):

        if email in all_users:
            return all_users[email]

        return {'message':"user does not exist"}
