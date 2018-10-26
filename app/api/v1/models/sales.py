from .products  import all_Products

all_sales=[]
new_sale={}

# class for handling all sales data
class Sales(object):
    """
    This Class has methods for manipulation of sales data.
    """

    # method gets all data from all_sales dictionary
    def get_all(self):
        """
        This method gets all sales.
        returns:all sales.
        """

        return all_sales


    # method gets data for one sale
    def get_one(self,sale_id):
        """
        This method gets all attributes of a singke sale.
        param:sale_id.
        returns:all sales.
        raises:sale not found error.
        """
        for sale in all_sales:

            if sale_id == sale["sale_id"]:
                return sale
            return False    




    # method adds new sale to all_sales dictionary
    def add_sale(self,sale_id,item,value,time):

        """
        This method adds new salesself.
        param1:sale_id
        param2:item.
        paeram3:value.
        param4:time.

        returns: sale added messageself.
        raises:sale already done message.
        raises:product not available message.
        """
        new_sale['sale_id']=sale_id
        new_sale['item']=item
        new_sale['value']=value
        new_sale['time']=time
        all_sales.append(new_sale)

        return {'message':'sale completed'}
