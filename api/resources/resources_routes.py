from flask_restful import Resource
from flask import request,session,redirect,url_for
from api.db.table import Usertable
from api.db.validation import UsertableForm
from api.db.db import db
from api.logg_ing.logg_f import Loggercheck
from api.config.auth import Token
from flask_jwt_extended import jwt_required
from api.db.schemas import Schemas
from werkzeug.datastructures import MultiDict
class Home(Resource):
    def __init__(self):
        pass

    def get(self):
        return "You are in Home now"

class Login(Resource):
    def __init__(self):
        pass

    def post(self):
        sc=Schemas()
        username=request.json.get('username').strip()
        password=request.json.get('password').strip()
        user=self.query_user(username)
        log=Loggercheck()
        tok=Token(username)

        if user and user.verify_pass(password):
            user_s=sc.dump(user)
            # passw=sc.dump(user.password)
            if tok.check_token_expired(tok.new_tok()):
                new_token=tok.refresh_token()
                log.logg_check(message="Token Refreshed")
            log.logg_check(message="login_sucesfull")
            return {'message':'LOGIN SUCCESSFUL','token':tok.new_tok(),'username_details':user_s['username']},201
        elif user is None:
            log.logg_check(message="User not found and redirected to register page")
            return redirect(url_for('signup'))
        else:
            log.logg_check(message="BAD CRED")
            return {'message':'BAD CRED'},401
    @staticmethod
    def query_user(username):
       user_q= Usertable.query.filter_by(username=username).first()
       return user_q




class Logout(Resource):
    def __init__(self):
        pass

    def post(self):
        session.pop('username',None)
        return redirect(url_for('home'))

class Signup(Resource):
    def __init__(self):
        pass

    def post(self):
        data = MultiDict(request.get_json())
        vali=UsertableForm(data)
        if not vali.validate():
            return vali.errors
        new_user=Usertable()
        new_user.username=data.get('username').strip()
        new_user.password=data.get('password').strip()
        new_user.generate_hash()
        new_user.email=data.get('email').strip()
        new_user.phone=data.get('phone').strip()
        if Usertable.query.filter_by(username=new_user.username).first():
            return "User exists",400

        if not (new_user.username and new_user.password and new_user.email and new_user.phone):
            return "Missing fields",400

            # user=Usertable(username,password,email,phone)
        db.session.add(new_user)
        db.session.commit()

        return "User added",201



class Con(Resource):
    def __init__(self):
        pass

    @jwt_required(refresh=True)
    def get(self):
        return {'message':"You are in safe hands"}


class Getall(Resource):
    @jwt_required()
    def get(self):
        user=Usertable.query.all()
        return {'data':[user.to_dict() for user in user]}



