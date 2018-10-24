from flask import Flask, jsonify, request
from flask_restful import Resource
import time
import datetime

from ..models.sales import Sales, all_sales

sale_object = Sales()
# endpoint class for sales
class SalesApi(Resource):



    def post(self):
        data=request.get_json()

        if not data:
            return {'message':'fields cannot be empty'}

        sale_id = len(all_sales) + 1
        item = data.get('item')
        value = (data.get('value'))
        time = data.get('time')
        timeformat = "%H:%M:%S"

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
        sales=sale_object.get_all()
        response=jsonify({"sale":sales,"message":"The above sales were found"})
        response.status_code=200

        return response



    # endpoint class for geting one sale

class SingleSaleApi(Resource):

    def get(self,sale_id):
        single_sale=sale_object.get_one(sale_id)
        response = jsonify({"sale":single_sale,"message":"The above sale was found"})
        response.status_code=200

        return response
