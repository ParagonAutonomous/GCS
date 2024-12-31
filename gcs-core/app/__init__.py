from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__version__ = "0.1.0"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")

    db.init_app(app)

    with app.app_context():
        from app import models
        db.create_all()

    return app