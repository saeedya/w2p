from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)

    # Load configuration from environment variables
    app.config.from_object(Config)

    # # Register blueprints
    # from .views import main_blueprint
    # app.register_blueprint(main_blueprint)

    return app