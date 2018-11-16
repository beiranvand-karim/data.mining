from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgres://karim:karim852654@127.0.0.1:5432/opinion_mining"

db = create_engine(db_string)
base = declarative_base()


class Film(base):
    __tablename__ = 'films'

    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

doctor_strange = Film(title="Doctor Strange", director="Scott Didrikson", year="2016")
session.add(doctor_strange)
session.commit()

films = session.query(Film)
for film in films:
    print(film.title)

doctor_strange.title = "Some2016Film"
session.commit()

session.delete(doctor_strange)
session.commit()
session.close()
