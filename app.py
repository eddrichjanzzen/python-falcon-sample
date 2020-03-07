import falcon
import json_utils
from decouple import config
from product_resource import ProductResource


# Declare Falcon Middleware 
# RequireJSON will always make sure the application data is in JSON format
# JSONtranslator will translate the stream data from falcon into JSON format
api = falcon.API(middleware=[
			json_utils.RequireJSON(),
			json_utils.JSONtranslator(),
		])

# Define the resource classes and the routes here:
# Note that the classes used here, references the folder called api_resources      

product = ProductResource()

api.add_route('/products', product)
api.add_route('/products/{product_id}', product, suffix="product")