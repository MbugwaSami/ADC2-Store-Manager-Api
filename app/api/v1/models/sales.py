from .products  import all_Products

all_sales={}
new_sale={}

# class for handling all sales data
class Sales(object):

    # method gets all data from all_sales dictionary
    def get_all(self):

        return all_sales


    # method gets data for one sale
    def get_one(self,sale_id):
        if sale_id in all_sales:
            return all_sales[sale_id]

        return {'message':'sale not found'}



    # method adds new sale to all_sales dictionary
    def add_sale(self,sale_id,item,value,time):

        if sale_id in all_sales:
            return {'message':'It seems this sale has already been made'}

        for sale_item in all_Products:

            if item != all_Products[sale_item]['product_name']:

                 return {'message':'Product not available'}

        new_sale['item']=item
        new_sale['value']=value
        new_sale['time']=time

        all_sales[sale_id]=new_sale

        return {'message':'sale completed'}
