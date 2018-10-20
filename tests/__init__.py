import unittest

from app import create_app
from instance.config import app_config

class TestBase(unittest.TestCase):

    def setUp(self):
        config="testing"
        self.app = create_app(config)
        self.client = self.app.test_client()

        self.test_product =dict(
        product_id = 1,
        product_name = "khaki Trouser",
        description = "White size 32",
        price = 300,
        stock = 100,
        minStock = 10
        )

        self.test_sale = dict(
        sale_id = 1,
        items = 3,
        value = 3000,
        profit = 600,
        time = 10-18-2018
        )
