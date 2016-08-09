from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from app import db

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Set your classes here.

'''
class User(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
'''

class Type(Base):
    __tablename__ = 'Types'

    id = db.Column(db.Integer, primary_key=True)
    typestr = db.Column(db.String, unique=True)
    def __init__(self, typestr ):
        self.typestr= typestr


class Advantage(Base):
    __tablename__= 'Advantages'

    id = db.Column(db.Integer, primary_key=True)
    strong = db.Column(db.String)
    weak = db.Column(db.String)
    modifier = db.Column(db.Integer)

# Create tables.
Base.metadata.create_all(bind=engine)
