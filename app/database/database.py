from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:12345@localhost/hbd"

# setup the database engine
engine =  create_engine(DATABASE_URL, echo =True)

# declare the base for our ORM classes
Base = declarative_base()

# create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)