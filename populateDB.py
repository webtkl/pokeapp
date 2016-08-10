from app import db
from models import Type,AdvantageChart

file=open("typeChart.txt")

for line in file:
    fields=line.split("#")
    if len(fields)>5:
        immunity_string=fields[5]
    else:
        immunity_string=""
    t = Type(fields[0])
    c = AdvantageChart(fields[0],fields[1],fields[2],fields[3],fields[4],immunity_string)

    db.session.add(t)
    db.session.add(c)
    db.session.commit()

file.close()
