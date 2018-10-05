#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#This class initializes the database connection
class PsqlDatabaseConnection:
    def __init__(self, user, password, host, port, dbname):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = dbname
        self.engine = None

    # The connect function will try to establish a connection to the database
    def connect(self):
        try:
            conn_string = "postgresql://%s:%s@%s:%s/%s" % (
                                self.user, 
                                self.password, 
                                self.host, 
                                self.port, 
                                self.dbname
                            )

            print("Connecting to database\n	->%s" % (conn_string))
           
            # make echo true to send all the sql to stdout
            self.engine = create_engine(conn_string, echo=True)

            Session = sessionmaker(self.engine)  
            session = Session()
            session.execute('SELECT 1')
            
            print("Successfully connected!")
        
        except Exception as e:
            print('ERROR: \n', e)


        return self.engine

