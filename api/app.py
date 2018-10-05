import json
import falcon
from api import db_utils
from decouple import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from api.models import (Player)

# Establish the database connection
# Create connection object
conn = db_utils.PsqlDatabaseConnection(
            config('DB_USER', default='postgres'), 
            config('DB_PASSWORD', default=''), 
            config('DB_HOST', default='db'), 
            config('DB_PORT', default='5432'), 
            config('DB_NAME', default='postgres')
        )

# Create the engine and call connect function
engine = conn.connect()

# Create the session
session_factory = sessionmaker(bind=engine)  
Session = scoped_session(session_factory)

#Declare Falcon Middleware
api = falcon.API(middleware=[
            db_utils.SQLAlchemySessionManager(Session),
        ])


class PlayerResource(object):

    def on_get(self, req, resp):       
        query = self.session.query(Player).all()
        doc = [row.as_dict() for row in query]
        
        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, indent=2)

        resp.status = falcon.HTTP_200


players = PlayerResource()
api.add_route('/players', players)