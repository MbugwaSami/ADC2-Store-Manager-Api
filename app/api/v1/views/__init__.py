from flask import Blueprint
from flask_restful import Api, Resource

# import the endpoint classes
from .products_endpoints import ProductsApi, SingleProductApi
from .sales_endpoints import SalesApi, SingleSaleApi
from .users_endpoints import UsersApi, SingleUserApi

# create the app Blueprint
app_v1 = Blueprint('app_v1',__name__, url_prefix="/api/v1")
api_v1 = Api(app_v1)

# add resources to the app Blueprint
api_v1.add_resource(ProductsApi,'/products')
api_v1.add_resource(SingleProductApi,'/products/<int:product_id>')
api_v1.add_resource(SalesApi,'/sales')
api_v1.add_resource(SingleSaleApi,'/sales/<int:sale_id>')
api_v1.add_resource(UsersApi,'/users/register','/users')
api_v1.add_resource(SingleUserApi,'/user/login','/user/<email>')