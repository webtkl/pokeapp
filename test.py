from app import db
from flask import jsonify
from models import Type, AdvantageChart
from pprint import pprint

type='Dragon'

c = AdvantageChart.query.filter_by(type=type).first()

print c.serialize()




