from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class AppContext(object):
    _app = None

    def __init__(self):
        raise Exception('call instance()')

    @classmethod
    def get(cls):
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
    def get(cls):
        if cls._db is None:
            cls._db = SQLAlchemy()
        if cls._app is None:
            cls._app = AppContext.get()
        return cls._db

