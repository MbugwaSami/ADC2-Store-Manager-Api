from flask import Blueprint
from flask_restful import Api, Resource

# import the endpoint classes
from .products_endpoints import ProductsApi, SingleProductApi

# create the app Blueprint
app_v1 = Blueprint('app_v1',__name__, url_prefix="/api/v1")
api_v1 = Api(app_v1)

# add resources to the app Blueprint
api_v1.add_resource(ProductsApi,'/products')
api_v1.add_resource(SingleProductApi,'/products/<int:product_id>')