from flask import Flask, jsonify, request
from flask_restful import Resource

from ..models.sales import Sales, all_sales

sale_object = Sales()
# endpoint class for sales
class SalesApi(Resource):



    def post(self):
        data=request.get_json()

        sale_id = len(all_sales) + 1
        items = data.get('items')
        value = data.get('value')
        profit = data.get('profit')
        time = data.get('time')

        response = jsonify(sale_object.add_sale(sale_id,items,value,profit,time))
        response.status_code = 201

        return response