from app import app
from db import db

db.init_app(app)

@app.before_first_request  #affects method before it, before the first request in the app. From Flask
def create_tables():
    db.create_all() #creates the sqlte://data.db files from line 11