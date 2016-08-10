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


class AdvantageChart(Base):
    __tablename__= 'Chart'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    strongAgainst = db.Column(db.String)
    weakAgainst = db.Column(db.String)
    resistantTo = db.Column(db.String)
    vulnerableTo = db.Column(db.String)
    immuneTo = db.Column(db.String)

    def __init__(self, type, str, weak, res, vul, imm='NULL'):
        self.type=type
        self.strongAgainst=str
        self.weakAgainst=weak
        self.resistantTo=res
        self.vulnerableTo=vul
        self.immuneTo=imm

    def serialize(self):
        return {
        'type':self.type,
        'str':self.strongAgainst,
        'weak':self.weakAgainst,
        'res':self.resistantTo,
        'vul':self.vulnerableTo,
        'imm':self.immuneTo
        }

# Create tables.
Base.metadata.create_all(bind=engine)
