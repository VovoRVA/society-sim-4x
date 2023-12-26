from constructors import AppContext, DbContext

app = AppContext.get()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_file.db"
db = DbContext.get()
db.init_app(app)
