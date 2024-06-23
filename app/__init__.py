from flask import Flask
from .models import db
from .main import main
from .main_html import main_html
from config import app_config

def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config)

    db.init_app(app)

    # Registracija Blueprintova
    app.register_blueprint(main)
    app.register_blueprint(main_html)

    return app
