import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'e_coaching.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Postavite varijablu okruženja FLASK_ENV na 'development' ili 'production' kako biste odabrali odgovarajuću konfiguraciju
flask_env = os.getenv('FLASK_ENV', 'development')
if flask_env == 'production':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()
