from flask import Flask, jsonify, request
from flask_restful import Resource

from ..models.products import Products, all_Products

# create a producrs object
products_object = Products()

# endpoint class for products
class ProductsApi(Resource):
    """
    This class endpoints for products.
    """

    def post(self):
        """"
        This method posts data of a product.
        returns: json response.
        raises:product fields cannot be empty.
        raises:product name cannot be empty error.
        raises:price must be a number message.
        raises:stock must be an integer messager.


        """


        data=request.get_json()

        if not data:
            return {'message':'fields can not be empty'}

        product_id = len(all_Products)+1
        product_name = data.get('product_name')
        description = data.get('description')
        price = data.get('price')
        stock = data.get('stock')
        minStock = data.get('minStock')

        if not product_name or product_name.isspace():

            return {'message':'Product name cannot be empty'}

        if products_object.check(product_name):
            return {'message':'Product with this name already exists'}

        if type(stock) is not int:

            return {'message':'Stock must be an integer'}

        if type(minStock) is not int:

            return {'message':'minimum Stock must be an integer'}

        try:
                price = float(price)
        except ValueError:

            return {'message':'Product price must be a number'}

        added_product = products_object.add_product(product_id,product_name,description,price,stock,minStock)
        response = jsonify(added_product)
        response.status_code = 201

        return response

    def get(self):

        """"
        This method gets data of all products.
        returns:items details
        """
        products_list = products_object.get_all()
        response = jsonify({"products":products_list,"message":"The following items were found"})
        response.status_code = 200
        return response



  # endpoint class for geting one product
class SingleProductApi(Resource):

    def get(self,product_id):
        """
        This method gets data of a single product.
        returns: details of a single product.
        """

        response = jsonify({"product":products_object.get_one(product_id),"message":"The following item was found"})
        response.status_code = 200

        return response
