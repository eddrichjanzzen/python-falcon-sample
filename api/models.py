from decouple import config
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
#Test table
class Player(Base):  
	__tablename__ = 'players'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	rank = Column(Integer)
	country = Column(String)

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Gender(Base):
	__tablename__ = 'genders'
	id = Column(Integer, primary_key=True)
	gender = Column(String)
