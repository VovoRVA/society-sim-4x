from main import app, db
from db_functions import DBEngine as DBE


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    age = db.Column(db.String, nullable=False)
    skills = db.Column(db.String, nullable=False)
    traits = db.Column(db.String, nullable=False)
    land = db.Column(db.Integer, db.ForeignKey('land.id'))
    region = db.Column(db.Integer, db.ForeignKey('region.id'))


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    climate_type = db.Column(db.String, nullable=False)
    x_position = db.Column(db.Integer, nullable=False)
    y_position = db.Column(db.Integer, nullable=False)
    lands = db.relationship('Land', backref='Region')
    persons = db.relationship('Person', backref='Region')


class Land(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    land_type = db.Column(db.String, nullable=False)
    x_position = db.Column(db.Integer, nullable=False)
    y_position = db.Column(db.Integer, nullable=False)
    persons = db.relationship('Person', backref='Land')
    region = db.Column(db.Integer, db.ForeignKey('region.id'))


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)


DBE.update()


