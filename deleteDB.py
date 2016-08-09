from app import db
from models import Type, Advantage
from pprint import pprint


Advantage.query.delete()
db.session.commit()
Type.query.delete()
db.session.commit()

