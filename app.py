from flask import Flask
from app.models import db
from app.main import main
from app.main_html import main_html
from config import app_config

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(app_config)

    db.init_app(app)

    # Registracija Blueprintova
    app.register_blueprint(main)
    app.register_blueprint(main_html)

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
