from flask import Flask, jsonify, request
from flask_restful import Resource

from ..models.products import Products, all_Products

# create a producrs object
products_object = Products()

# endpoint class for products
class ProductsApi(Resource):

    def post(self):

        data=request.get_json()

        product_id = len(all_Products)+1
        product_name = data.get('product_name')
        description = data.get('description')
        price = data.get('price')
        stock = data.get('stock')
        minStock = data.get('minStock')


        response = jsonify(products_object.add_product(product_id,product_name,description,price,stock,minStock))
        response.status_code = 201

        return response

    def get(self):
        products_list = products_object.get_all()
        response = jsonify(products_list)
        response.status_code = 200
        return response



  # endpoint class for geting one product
class SingleProductApi(Resource):

    def get(self,product_id):

        response = jsonify(products_object.get_one(product_id))
        response.status_code = 200

        return response      