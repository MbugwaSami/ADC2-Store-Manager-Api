import json

from tests import TestBase


class TestProducts(TestBase):

    def test_post_product(self):

        response = self.client.post(
        '/api/v1/products',
        data = json.dumps(self.test_product),
        content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)


    def test_get_products(self):

        response = self.client.post(
        '/api/v1/products',
        data = json.dumps(self.test_product),
        content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/v1/products')

        self.assertEqual(response.status_code, 200)


    def test_get_one_product(self):

        response = self.client.post(
        '/api/v1/products',
        data = json.dumps(self.test_product),
        content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/v1/products/1')

        self.assertEqual(response.status_code, 200)

    def test_validate_product_name(self):

       response = self.client.post(
        '/api/v1/products',
        data = json.dumps(self.test_product),
        content_type='application/json'
        )

       response_data = json.loads(response.data)
       self.assertEqual("Succesfuly added a product",response_data["message"])


       response = self.client.post(
        '/api/v1/products',
        data = json.dumps(self.test_product),
        content_type='application/json'
        )

       response_data = json.loads(response.data)
       self.assertEqual("Product with this name already exists",response_data["message"])


    def test_price_is_number():

        response = self.client.post(
        '/api/v1/products',
        data = json.dumps(self.test_product1),
        content_type='application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Product price must be a number",response_data["message"])  


     
    def test_stock_is_number():

        response = self.client.post(
        '/api/v1/products',
        data = json.dumps(self.test_product2),
        content_type='application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Stock must be an integer",response_data["message"])

        response = self.client.post(
        '/api/v1/products',
        data = json.dumps(self.test_product3),
        content_type='application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("minimum Stock must be an integer",response_data["message"])        
             
      
             

        

              
