import os
import ujson
import falcon
import requests
from custom_logger import setup_logger
from datetime import datetime
from decouple import config
from pprint import pprint, pformat

logger = setup_logger('ProductResource Logger')


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'products.json')

# load products static db from json file
with open(my_file) as f:
    products = ujson.load(f)


class ProductResource(object):
	
	def on_get(self, req, resp):

		try:
			logger.info("Performing get all products...")
			
			resp.body = ujson.dumps({'products': products})
			resp.status = falcon.HTTP_200

		except Exception as e:

			logger.error(e, exc_info=True)

			resp.body = ujson.dumps({"error": e})
			resp.status = falcon.HTTP_502


	def on_get_product(self, req, resp, product_id):

		try:
			logger.info("Performing get product...")
			
			product = [p for p in products if str(p['id']) == str(product_id)]

			if product == []:

				resp.body = ujson.dumps({'error': 'product not found.'})
				resp.status = falcon.HTTP_404

			else: 

				resp.body = ujson.dumps({'products': product[0]})
				resp.status = falcon.HTTP_200



		except Exception as e:

			logger.error(e, exc_info=True)

			resp.body = ujson.dumps({"error": e})
			resp.status = falcon.HTTP_502


	def on_post(self, req, resp):

		try:
			logger.info("Performing post request...")

			body = req.context['request']

			product = {
				'id': body['id'],
				'name': body['name'],
				'stock' : body['stock'],
				'price' : body['price']
			}

			products.append(product)

			resp.body = ujson.dumps({
				'products': product,
				'status': 'CREATED OK'
			})


			resp.status = falcon.HTTP_200

		except Exception as e:

			logger.error(e, exc_info=True)

			resp.body = ujson.dumps({"error": "connection error"})
			resp.status = falcon.HTTP_502


	def on_put_product(self, req, resp, product_id):
		
		try:
			logger.info("Performing put request...")

			body = req.context['request']

			product = [p for p in products if str(p['id']) == str(product_id)]

			if product == []:

				resp.body = ujson.dumps({'error': 'product not found.'})
				resp.status = falcon.HTTP_404

			else: 

				product[0]['name'] = body['name']
				product[0]['stock'] = body['stock']
				product[0]['price'] = body['price']

				resp.body = ujson.dumps({
					'products': product,
					'status': 'UPDATED OK'
				})

				resp.status = falcon.HTTP_200

		except Exception as e:

			logger.error(e, exc_info=True)

			resp.body = ujson.dumps({"error": e})
			resp.status = falcon.HTTP_502

	def on_delete_product(self, req, resp, product_id):

		try:
			logger.info("Performing delete request...")

			product = [p for p in products if str(p['id']) == str(product_id)]

			if product == []:

				resp.body = ujson.dumps({'error': 'product not found.'})
				resp.status = falcon.HTTP_404

			else:

				products.remove(product[0])

				resp.body = ujson.dumps({
					'products': product,
					'status': 'DELETED OK'
				})

			resp.status = falcon.HTTP_200

		except Exception as e:

			logger.error(e, exc_info=True)

			resp.body = ujson.dumps({"error": e})
			resp.status = falcon.HTTP_502







