from app import db
from models import Type, Chart
from pprint import pprint

'''
Chart.query.delete()
db.session.commit()
Type.query.delete()
db.session.commit()
'''


db.session.query(Type).delete()
db.session.query(Chart).delete()
db.session.commit()