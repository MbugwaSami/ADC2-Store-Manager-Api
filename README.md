# ADC2_Store_Manager

[![Build Status](https://travis-ci.org/MbugwaSami/ADC2-Store-Manager-Api.svg?branch=develop)](https://travis-ci.org/MbugwaSami/ADC2-Store-Manager-Api)
![Coverage Status](https://coveralls.io/repos/github/MbugwaSami/ADC2-Store-Manager-Api/badge.svg?branch=develop)

This repository  contains API endpoints for  Store Manager application. Store Manager application is an application that helps small scale stalls manage their sales and inventory.The application has two level of users, the store owner who is also the admin and the store attendant.
The Admin is responsible for adding new products and creating user accounts and the store attendant is responsible for making new sales.

### The minimum required endpoint are  
| Endpoint | Description |
| --- | --- |
|GET /Fetch all products	| This endpoint gets all available products in the system.Accesed to both the Admin and the store attendant|
|GET /Fetch a single product record	| This endpoint gets a specific product using the product’s id. Accesed by the Admin and store attendant|
|GET /Fetch all sale records.|This endpoint gets all sales done by all the store attendants.Accesed  by the store owner/admin |
|GET /sales/Fetch a single sale record	|This endpoint gets a specific sale record using the sale record Id. Accesed by the store owner/admin and the creator (store attendant) of the specific sale record.|
|POST /Create a product | This endpoint creates a new product record. Accessed by  the store owner/admin only.|
|POST /Create a sale order|This endpoint creates a sale record. Accessed by the store attendant|

### How to run the application

- open a git bash
- git clone https://github.com/MbugwaSami/ADC2-Store-Manager-Api.git
- cd ADC2-Store-Manager-Api
- pip install virtualenv
- python -m venv venv
- source venv/scripts/activate
- pip install flask
- pip install flask-restful
- python run.py
- Test the endpoints url on postaman


### How to run the tests 

- open a git bash
- git clone https://github.com/MbugwaSami/ADC2-Store-Manager-Api.git
- cd ADC2-Store-Manager-Api/
- pip install virtualenv
- python -m venv venv
- source venv/scripts/activate
- pip install flask
- pip install flask-restful
- pip install pytest
- pip install pylint
- cd tests
- pytest test_product.py to run the products tests
- pytest test_sales.py to run the sales tests
- pytest test_auths.py to run the auth tests


