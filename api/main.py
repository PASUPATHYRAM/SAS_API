from flask import Flask
from api.db.db import db
from api.config.db_config import SQLALCHEMY_DATABASE_URI
from api.routes.routes import generate_routes
from api.config.auth import jwt
from datetime import timedelta
from json import JSONEncoder
import datetime


class CustomEncoder(JSONEncoder):
    def default(self,obj):
        if isinstance(obj,datetime.datetime):
            return obj.isoformat()
        return super().default(obj)
def create_app():
    app=Flask(__name__)
    app.config['DEBUG']=True
    app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY']='RAM@1803#qwe'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    # app.json_encoder=CustomEncoder


    with app.app_context():
        generate_routes(app)
        db.init_app(app)
        jwt.init_app(app)
        db.create_all()
    return app

if __name__=="__main__":
    app=create_app()
    app.run(port=3020,host='localhost')


