from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class AppContext(object):
    _app = None

    def __init__(self):
        raise Exception('call instance()')

    @classmethod
    def app(cls):
        if cls._app is None:
            cls._app = Flask(__name__)
            # more init opration here
        return cls._app


class DbContext(object):
    _app = None
    _db = None

    def __init__(self):
        raise Exception('call instance()')

    @classmethod
    def db(cls):
        if cls._db is None:
            cls._db = SQLAlchemy()
        if cls._app is None:
            cls._app = AppContext.app()
        return cls._db

    @classmethod
    def batch_insert(cls, items: list):
        with cls._app.app_context():
            for item in items:
                cls._db.session.add(item)
            cls._db.session.commit()
            cls._db.create_all()
