from flask import Flask

def create_app():
    app = Flask(__name__)

    # # Load configuration from environment variables
    # app.config.from_object(os.environ.get('FLASK_CONFIG', 'config.Config'))

    # # Register blueprints
    # from .views import main_blueprint
    # app.register_blueprint(main_blueprint)

    return app