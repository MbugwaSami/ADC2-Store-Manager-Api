all_Products = {}
product_details = {}


# class for handling product data
class Products(object):

    # method gets all products from all_Products dictionary
    def get_all(self):

        return all_Products


    # method gets data for one product
    def get_one(self,product_id):

        if product_id in all_Products:

            return all_Products[product_id]

        return {'message':'product not found'}


    # method for adding data to all_sales dictionary
    def add_product(self,product_id,product_name,description,price,stock,minStock):

        if product_id in all_Products:

            return {'message':'This product already exists'}

        for item in all_Products:

            if product_name == all_Products[item]['product_name']:

                
                return {'message':'Product with this name already exists'}
        
        product_details['product_name'] = product_name
        product_details['price'] = price
        product_details['description'] = description
        product_details['stock'] = stock
        product_details['minStock'] = minStock

        all_Products[product_id] = product_details
        
        return {'message':'product succesfully added'}

