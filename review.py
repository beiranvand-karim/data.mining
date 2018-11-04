from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from constants import db_string


db = create_engine(db_string)
base = declarative_base()


class Review(base):
    __tablename__ = 'gansevoort_reviews'

    id = Column(String, primary_key=True)
    date = Column(String)
    review = Column(String)


base.metadata.create_all(db)

