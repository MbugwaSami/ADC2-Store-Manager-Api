from flask import Flask, jsonify, request
from flask_restful import Resource

from ..models.sales import Sales, all_sales

sale_object = Sales()
# endpoint class for sales
class SalesApi(Resource):



    def post(self):
        data=request.get_json()

        sale_id = len(all_sales) + 1
        item = data.get('item')
        value = data.get('value')
        time = data.get('time')

        response = jsonify(sale_object.add_sale(sale_id,item,value,time))
        response.status_code = 201

        return response


    def get(self):
        sales=sale_object.get_all()
        response=jsonify(sales)
        response.status_code=200

        return response    



    # endpoint class for geting one sale

class SingleSaleApi(Resource):

    def get(self,sale_id):
        single_sale=sale_object.get_one(sale_id)
        response = jsonify(single_sale)
        response.status_code=200

        return response    