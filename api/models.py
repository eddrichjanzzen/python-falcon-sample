import db_connector
from decouple import config
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Establish the database connection
# Create connection object
conn = db_connector.PsqlDatabaseConnection(
			config('DB_USER', default='postgres'), 
			config('DB_PASSWORD', default=''), 
			config('DB_HOST', default='db'), 
			config('DB_PORT', default='5432'), 
			config('DB_NAME', default='postgres')
		)

# Create the engine and call connect function

engine = conn.connect()
Base = declarative_base()

#Test table
class Player(Base):  
	__tablename__ = 'players'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	rank = Column(Integer)
	country = Column(String)


Session = sessionmaker(engine)  
session = Session()

Base.metadata.create_all(engine)