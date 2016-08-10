from app import db
from models import Type, AdvantageChart
from pprint import pprint

'''
Chart.query.delete()
db.session.commit()
Type.query.delete()
db.session.commit()
'''


db.session.query(Type).delete()
db.session.query(AdvantageChart).delete()
db.session.commit()