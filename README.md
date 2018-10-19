# ADC2_Store_Manager

This repository  contains API endpoints for  Store Manager application.

The minimum required endpoint are  

GET /products	Fetch all products	Get all available products.

GET /products/	Fetch a single product record	Get a specific product using the product’s id.

GET /sales	Fetch all sale records	.Accesed only by the store owner/admin.

GET /sales/	Fetch a single sale record	Get a specific sale record using the sale record Id. Accesed by the store owner/admin and the creator (store attendant) of the specific sale record.

POST /products	Create a product	Create a new product record. Allowed for  the store owner/admin only.

POST /sales	Create a sale order	Create a sale record.
