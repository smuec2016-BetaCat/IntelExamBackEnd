from flask import Flask
from flask_restful import Api
from configs.config import (DB_HOST, DB_PORT, DB_SCHEMA, DB_USER)
from configs.database import db
from resources.CandidateApi import CandidateApi
from resources.addCandidateApi import addCandidateApi
from resources.LoginApi import LoginApi
from flask_cors import CORS

app = Flask(__name__)   # create app object
CORS(app)
api = Api(app)      # create api object
app.config["SQLALCHEMY_DATABASE_URI"] = \
    f"mysql+pymysql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_SCHEMA}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

with app.app_context():
    db.init_app(app)    # init db
    db.create_all()     # create tables

api.add_resource(CandidateApi, '/api/v0/candidate')
api.add_resource(addCandidateApi, '/add')
api.add_resource(LoginApi, '/api/v0/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

