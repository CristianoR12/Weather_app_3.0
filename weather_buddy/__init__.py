from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os 

db = SQLAlchemy()
DB_NAME = "database.db"

API_key = os.environ['secret_key']

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'any_key' 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views 

    app.register_blueprint(views, url_prefix='/')
    
    from . models import City

    create_database(app)

    return app

def create_database(app):
    if not path.exists('weather_buddy/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')