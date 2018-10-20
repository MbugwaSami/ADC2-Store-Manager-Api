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