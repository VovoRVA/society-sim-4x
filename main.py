from constructors import AppContext, DbContext

app = AppContext.app()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_file.db"
db = DbContext.db()
db.init_app(app)



print(app)