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
        data = json.dumps(self.test_sales),
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
