from flask import Flask
from config import Config

def create_app(config_class=Config):
  app: Flask = Flask(__name__)
  app.config.from_object(config_class)

  # Initialize flask extensions here

  # Register blueprints here
  from src.main import main_blueprint as main_bp
  from src.errors import errors_blueprint as errors_bp
  from src.auth import authentication_blueprint as auth_bp

  app.register_blueprint(main_bp)
  app.register_blueprint(errors_bp)
  app.register_blueprint(auth_bp)

  return app
