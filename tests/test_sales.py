import json

from tests import TestBase


class TestSales(TestBase):



    def test_post_sales(self):

        response = self.client.post(
        '/api/v1/sales',
        data = json.dumps(self.test_sale),
        content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)


    def test_get_sales(self):

        response = self.client.post(
        '/api/v1/sales',
        data = json.dumps(self.test_sale),
        content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/v1/sales')

        self.assertEqual(response.status_code, 200)


    def test_get_one_sale(self):

        response = self.client.post(
        '/api/v1/sales',
        data = json.dumps(self.test_sale),
        content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/v1/sales/1')

        self.assertEqual(response.status_code, 200)

    def tests_validate_sales_value(self):

        response = self.client.post(
        '/api/v1/sales',
        data = json.dumps(self.test_sale1),
        content_type='application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Value must me a number",response_data["message"])

    def test_product_sold_exist(self):


        response = self.client.post(
        '/api/v1/products',
        data = json.dumps(self.test_product),
        content_type='application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Succesfuly added a product",response_data["message"])

        response = self.client.post(
        '/api/v1/sales',
        data = json.dumps(self.test_sale),
        content_type='application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Product not available",response_data["message"])


    def test_time_is_valid(self):


        response = self.client.post(
        '/api/v1/sales',
        data = json.dumps(self.test_sale2),
        content_type='application/json'
        )


        response_data = json.loads(response.data)
        self.assertEqual("Please enter a valid time string",response_data["message"])










        
