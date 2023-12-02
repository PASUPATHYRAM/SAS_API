from flask_jwt_extended import JWTManager,create_access_token,create_refresh_token,decode_token,get_jwt_identity,jwt_required
from flask import jsonify
from datetime import datetime
jwt=JWTManager()

class Token:
    def __init__(self,username):
        self.username=username
        self.new_access=create_access_token(identity=self.username)
        self.renew_acces = create_refresh_token(identity=self.username)
    def new_tok(self):
        return self.new_access
    def rene_tok(self):
        return self.renew_acces

    @staticmethod
    def check_token_expired(token):
        decode=decode_token(token)
        exp_date=decode['exp']
        current_time=datetime.timestamp(datetime.now())
        return current_time>exp_date

    @staticmethod
    @jwt_required(refresh=True)
    def refresh_token():
        current_user=get_jwt_identity()
        new_token=create_access_token(current_user)
        return new_token






