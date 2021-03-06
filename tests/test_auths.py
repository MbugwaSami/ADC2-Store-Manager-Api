import json

from tests import TestBase

# class for testing test_user
class TestAuths(TestBase):

     # test user is created
    def test_create_account(self):

        response = self.client.post(
        '/api/v1/users',
        data = json.dumps(self.test_user),
        content_type = 'application/json'
        )

        self.assertEqual(response.status_code, 201)

        # test user is unique
        response = self.client.post(
        '/api/v1/users',
        data = json.dumps(self.test_user),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Email already registered",response_data["message"])




    def test_get_all_users(self):

        response = self.client.post(
        '/api/v1/users',
        data = json.dumps(self.test_user),
        content_type = 'application/json'
        )


        response = self.client.get('/api/v1/users')

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.data)
        self.assertEqual("This are the users in the system",response_data["message"])


    def test_user_login(self):

            response = self.client.post(
            '/api/v1/users',
            data = json.dumps(self.test_user),
            content_type = 'application/json'
            )

            response = self.client.post(
            '/api/v1/user/login',
            data = json.dumps(self.test_login),
            content_type = 'application/json'
            )

            self.assertEqual(response.status_code, 200)

            response_data = json.loads(response.data)



    def  test_email_is_valid(self):


        response = self.client.post(
        '/api/v1/users',
        data = json.dumps(self.test_user1),
        content_type = 'application/json'
        )


        response_data = json.loads(response.data)
        self.assertEqual("Please enter a valid email address",response_data["message"])




    def test_password_strength(self):


        response = self.client.post(
        '/api/v1/users',
        data = json.dumps(self.test_user2),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Password does not meet the strength criteria",response_data["message"])


    def test_validate_roles(self):

        response = self.client.post(
        '/api/v1/users',
        data = json.dumps(self.test_user3),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Roles can only be admin and store attendant",response_data["message"])
