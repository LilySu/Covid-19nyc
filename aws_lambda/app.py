from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from os import environ
from sql_queries.sql_counties import execute_scrape_counties_wikipedia


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class countyTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(80), unique=True)
    confirmed = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    recoveries = db.Column(db.Integer)
    population = db.Column(db.String(11))
    deaths2confirmed = db.Column(db.Float)
    confirmed2population = db.Column(db.Float)
    lastupdated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return "<countyTable(id='%s')>" % self.id

@app.route('/')
def index():
    execute_scrape_counties_wikipedia()
    return "Hello"


if __name__ == "__main__":
    app.run()