from main import app, db

class DBEngine():
    def __init__(self, app, db):
        self.app = app
        self.db = db

    @staticmethod
    def batch_insert(items: list):
        with app.app_context():
            for item in items:
                db.session.add(item)
            db.session.commit()
            db.create_all()

    @staticmethod
    def update():
        with app.app_context():
            db.create_all()

    @staticmethod
    def reflect():
        with app.app_context():
            print(db.reflect())

    @staticmethod
    def batch_remove():
        pass

