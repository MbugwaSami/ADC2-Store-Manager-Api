all_Products = []
product_details = {}


# class for handling product data
class Products(object):
    """
    This class has methods for manipulation of products data.
    """

    # method gets all products from all_Products dictionary
    def get_all(self):
        """
        This method gets details of all sales.
        return:all products details.
        """

        return all_Products


    # method gets data for one product
    def get_one(self,product_id):
        """
        This method gets details of one sale.
        param:product_id.
        return:one product details.
        raises: product not found message.
        """
        for item in all_Products:

            if product_id == item["product_id"]:
                return item


    # method for adding data to all_sales dictionary
    def add_product(self,product_id,product_name,description,price,stock,minStock):
        """
        This method adds new product.
        param1:produ_id
        param2:product_name.
        paeram3:price.
        param4:stock.
        param5:minStock.

        returns: product added message.
        raises:product existing message.
        """
        product_details['product_id']=product_id
        product_details['product_name'] = product_name
        product_details['price'] = price
        product_details['description'] = description
        product_details['stock'] = stock
        product_details['minStock'] = minStock

        all_Products.append(product_details)

        return {'message':'product succesfully added'}

    def check(self,product_name):
        for item in all_Products:

            if product_name == item["product_name"]:
                return True
