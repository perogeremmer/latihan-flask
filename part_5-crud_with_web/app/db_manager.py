from mongoengine import connect

class DatabaseManager(object):
    def __init__(self):
        self.db = None
    
    @staticmethod
    def open_database():
        
        from app.config import Config

        connect(
            db=Config.MONGODB_DB_NAME,
            username=Config.MONGODB_DB_USERNAME,
            password=Config.MONGODB_DB_PASSWORD,
            host=f'mongodb://{Config.MONGODB_DB_HOST}/{Config.MONGODB_DB_NAME}'
        )