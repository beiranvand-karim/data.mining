from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from constants import db_string

db = create_engine(db_string)

Session = sessionmaker(db)
session = Session()
