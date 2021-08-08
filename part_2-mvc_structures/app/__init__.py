
from flask import Flask
from flask_restful import Api # Memanggil library RESTful

app = Flask(__name__, template_folder='views')
api = Api(app, prefix='/api') # Melakukan inisialisasi terhadap library RESTful untuk route API
web = Api(app) # Melakukan inisialisasi terhadap library RESTful untuk route web

from app import routes
