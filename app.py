import falcon
import json_utils
from decouple import config

engine = create_engine(conn_string, echo=False)

# Create the session
session_factory = sessionmaker(bind=engine)  
Session = scoped_session(session_factory)

# Declare Falcon Middleware 
# RequireJSON will always make sure the application data is in JSON format
# JSONtranslator will translate the stream data from falcon into JSON format
api = falcon.API(middleware=[
			json_utils.RequireJSON(),
			json_utils.JSONtranslator(),
		])


# Define the resource classes and the routes here:
# Note that the classes used here, references the folder called api_resources      

api.add_route('/topup', topup)
api.add_route('/balance_inquiry', balanceinquiry)
api.add_route('/inquire_topup/{refnumber}', inquiretopup)