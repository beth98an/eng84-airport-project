# Main file
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
import os

from settings import ROOT_DIR, DB_URL

def create_db_engine():
    engine = create_engine(DB_URL)
    return engine

def create_db_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def initialise_database():
    engine = initialise_database()
    session = create_db_session(engine)
    Base = declarative_base()
    Base.metadata.create_all(engine)





def main():
    print("Project root: {}".format(ROOT_DIR))
    print("Database url: {}".format(DB_URL))

    # initialise_database()



if __name__ == '__main__':
    main()
