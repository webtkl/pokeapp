from app import db
from flask import jsonify
from models import Type, Chart
from pprint import pprint

type='Dragon'

c = Chart.query.filter_by(type=type)
typeinfo=c[0]\

pprint(typeinfo.__dict__)