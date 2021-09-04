from environs import Env

env = Env()
env.read_env()

from datetime import timedelta

class Config(object):
    APP_ENV = env.str("FLASK_ENV", default="development")
    FLASK_RUN_HOST = env.str("FLASK_RUN_HOST", default="localhost")
    FLASK_RUN_PORT = env.str("FLASK_RUN_PORT", default="5000")
    
    DEBUG = True if APP_ENV == "development" else False

    MONGODB_DB_NAME = env.str("MONGODB_DB_NAME", default="latihan_flask")
    MONGODB_DB_HOST = env.str("MONGODB_DB_HOST", default="localhost")
    MONGODB_DB_PORT = env.str("MONGODB_DB_PORT", default="27017")
    MONGODB_DB_USERNAME = env.str("MONGODB_DB_USERNAME", default="admin")
    MONGODB_DB_PASSWORD = env.str("MONGODB_DB_PASSWORD", default="admin")

    SECRET_KEY = env.str("SECRET_KEY", default="app-secret-key")
    
    JWT_SECRET_KEY = env.str("JWT_SECRET_KEY", default="jwt-secret-key")
    JWT_ALGORITHM = env.str("JWT_ALGORITHM", default="HS256")

    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = timedelta(days=3)