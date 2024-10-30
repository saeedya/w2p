from os import environ
class Config:

    # General Config
    ENV = environ.get("W2P_BACKEND_API_ENV", "production")

    DEBUG = bool(int(environ.get("W2P_BACKEND_API_DEBUG", "0")))

    TESTING = DEBUG