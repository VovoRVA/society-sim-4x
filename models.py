from main import db
from db_functions import DBEngine as DBE


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

DBE.update()
new_user = Person(username='Vovo5', email='dick@com')
DBE.batch_insert([new_user])
DBE.update()


