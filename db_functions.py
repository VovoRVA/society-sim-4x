from main import app, db


class DBEngine:
    def __init__(self):
        self.app = app
        self.db = db

    @staticmethod
    def batch_insert(items: list):
        with app.app_context():
            for item in items:
                db.session.add(item)
            db.session.commit()

    @staticmethod
    def update():
        with app.app_context():
            db.create_all()

    @staticmethod
    def reflect():
        with app.app_context():
            return db.reflect()

    @staticmethod
    def batch_remove():
        pass

    @staticmethod
    def dump_all():
        with app.app_context():
            db.drop_all()
            db.session.commit()

    def get_all(cls):
        with app.app_context():
            return cls.query.all()
