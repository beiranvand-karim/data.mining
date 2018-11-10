from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from constants import db_string


db = create_engine(db_string)
base = declarative_base()


class GansevoortReviewPOS(base):
    __tablename__ = 'gansevoort_review_pos'
    id = Column(Integer, primary_key=True)
    review_id = Column(Integer)
    sentence = Column(String)


base.metadata.create_all(db)
