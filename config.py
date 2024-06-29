import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

# Set the appropriate config based on environment
flask_env = os.getenv('FLASK_ENV', 'development')
if flask_env == 'production':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()
