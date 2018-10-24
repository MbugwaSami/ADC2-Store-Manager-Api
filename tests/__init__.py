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

        self.test_product1 =dict(
        product_id = 1,
        product_name = "kaki Trouser",
        description = "White size 32",
        price = "o",
        stock = 100,
        minStock = 10
        )

        self.test_product2 =dict(
        product_id = 1,
        product_name = "khaki Truser",
        description = "White size 32",
        price = 300,
        stock = "ee",
        minStock = 10
        )

        self.test_product3 =dict(
        product_id = 1,
        product_name = "khaki Trouser",
        description = "White size 32",
        price = 300,
        stock = 100,
        minStock = "22"
        )

        self.test_product4 =dict(
        product_id = 1,
        product_name = "",
        description = "White size 32",
        price = 300,
        stock = 100,
        minStock = "22"
        )
        self.test_product5 =dict(
        product_id = 1,
        product_name = "khaki shirt",
        description = "White size 32",
        price = 1,
        stock = 100,
        minStock = 10
        )

        self.test_product6 =dict(
        product_id = 1,
        product_name = "krt",
        description = "White size 32",
        price = 1,
        stock = 100,
        minStock = 10
        )



        self.test_sale = dict(
           sale_id = 1,
           item = "mutumba shirt",
           value = 3000.-0,
           time = "22:12:12"
           )

        self.test_sale1 = dict(
           sale_id = 1,
           item = "khaki shirt",
           value = "test",
           time = "10:18:20"
           )

        self.test_sale2 = dict(
           sale_id = 1,
           item = "khaki shirt",
           value = 2000,
           time = "2000"
           )
        self.test_sale3 = dict(
           sale_id = 1,
           item = "khaki Trouser",
           value = 2000,
           time = "10:18:20"
           )

        self.test_user = dict(
            email = "samimbugwa@gmail.com",
            names = "Sammy Njau",
            password = "Mwoboko10@",
            role = "attendant",
            )

        self.test_user1 = dict(
            email = "samimbugw",
            names = "Sammy Njau",
            password = "Mwoboko10@",
            role = "attendant",
            )

        self.test_user2 = dict(
            email = "sam@gmail.com",
            names = "Sammy Njau",
            password = "12345",
            role = "attendant",
            )

        self.test_user3 = dict(
            email = "sami@gmail.com",
            names = "Sammy Njau",
            password = "Mwoboko10@",
            role = "customer",
                        )

        self.test_login = dict(
            email = "samimbugwa@gmail.com",
            password = "12345")
