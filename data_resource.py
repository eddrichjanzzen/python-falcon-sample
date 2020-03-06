import json
import falcon
import requests
from custom_logger import setup_logger
from datetime import datetime
from decouple import config
from pprint import pprint, pformat

logger = setup_logger('BALANCE INQ')

class DataResource(object):
	
	def on_get(self, req, resp):

		try:
			logger.info("Performing get request...")
			
			
			# Return the response
			resp.body = json.dumps({'data': 'works'})
			resp.status = falcon.HTTP_200

			

		except requests.ConnectionError:
			
			logger.error("Connection error...")

			logger.error("Could be an issue with loadone endpoint? : ({})".format(self.url))

			resp.body = json.dumps({"error": "connection error please check loadone endpoint: ({})".format(self.url)})
			resp.status = falcon.HTTP_502


		except Exception as e:


			logger.error(e, exc_info=True)

			resp.body = json.dumps({'error' : 'Error in executing the transaction. The error has been saved in the db, please check response'})
			resp.status = falcon.HTTP_200