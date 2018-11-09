from flask import Flask, jsonify, request
from flask_restful import Resource
import time
import datetime

from ..models.sales import Sales, all_sales
from ..models.products import Products

product_object = Products()
sale_object = Sales()
# endpoint class for sales
class SalesApi(Resource):
    """
    This class has post and get methods for sales
    """



    def post(self):

        """"
        This method posts data of a sale.
        returns: json response.
        raises:sale fields cannot be empt.
        raises:value must be a number message.
        raises:time is invalid message.


        """
        data=request.get_json()

        if not data:
            return {'message':'fields cannot be empty'}

        sale_id = len(all_sales) + 1
        item = data.get('item')
        value = (data.get('value'))
        time = data.get('time')
        timeformat = "%H:%M:%S"
        if not product_object.check(item):
            return {'message':'Product not available'}

        try:
            validtime = datetime.datetime.strptime(time, timeformat)
        except ValueError:

            return {'message':'Please enter a valid time string'}

        try:
                value = float(value)
        except ValueError:

            return {'message':'Value must me a number'}

        response = jsonify(sale_object.add_sale(sale_id,item,value,validtime))
        response.status_code = 201

        return response


    def get(self):
        """
        This method gets data of a sale
        returns:list of sales.
        """
        sales=sale_object.get_all()
        response=jsonify({"sale":sales,"message":"The following sales were found"})
        response.status_code=200

        return response



    # endpoint class for geting one sale

class SingleSaleApi(Resource):

    def get(self,sale_id):
        """
        This method returns details of a single sale.
        param:sale_id
        """
        single_sale=sale_object.get_one(sale_id)
        response = jsonify({"sale":single_sale,"message":"The following sale was found"})
        response.status_code=200

        return response
