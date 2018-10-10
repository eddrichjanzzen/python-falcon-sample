import sys, os
sys.path.append(os.path.abspath(os.path.join('../..','api')))
import json
import db_utils
from decouple import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models import Player

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


# Base.metadata.create_all(engine)

def insert_data(file_name):
    json_data = open(file_name).read()
    data = json.loads(json_data)

    objects = []
    
    for p in data:
        objects.append(
            Player(name=p['name'], rank=p['rank'], country=p['country'])
        )
    
    Session.bulk_save_objects(objects)
    Session.commit()

    print("Successfully saved data.")


insert_data("/code/api/dummy_data/players.json")