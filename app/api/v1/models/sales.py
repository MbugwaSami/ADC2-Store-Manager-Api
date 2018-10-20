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
    def add_sale(self,sale_id,items,value,profit,time):

        if sale_id in all_sales:
            return {'message':'It seems this sale has already been made'}

        new_sale['items']=items
        new_sale['value']=value
        new_sale['profit']=profit
        new_sale['time']=time

        all_sales[sale_id]=new_sale

        return {'message':'sale completed'}
