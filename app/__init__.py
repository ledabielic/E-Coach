from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config)

    db.init_app(app)
    migrate = Migrate(app, db)

    from .main_html import main_html
    app.register_blueprint(main_html)

    return app
