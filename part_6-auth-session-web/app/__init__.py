
from flask import Flask, session
from flask_restful import Api # Memanggil library RESTful
from app.config import Config

app = Flask(
    __name__, 
    template_folder='views',
    static_url_path='/public', 
    static_folder='../public',
)
app.config.from_object(Config)

api = Api(app, prefix='/api') # Melakukan inisialisasi terhadap library RESTful untuk route API
web = Api(app) # Melakukan inisialisasi terhadap library RESTful untuk route web

from flask_session import Session
sess = Session()
sess.init_app(app)

from flask_jwt_extended import JWTManager
jwt = JWTManager(app)

from app.db_manager import DatabaseManager
DatabaseManager.open_database() # Melakukan inisialisasi terhadap library database

from app import routes
