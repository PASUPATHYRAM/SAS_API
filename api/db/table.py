import datetime
from json import JSONEncoder
from werkzeug.security import generate_password_hash,check_password_hash

from api.db.db import db

#creating table

class Usertable(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)

    username=db.Column(db.String(25),nullable=False)

    password = db.Column(db.String(12), nullable=False)

    email= db.Column(db.String(),nullable=False)

    phone=db.Column(db.Integer,nullable=False)

    role=db.Column(db.String(),default='user')

    created_on=db.Column(db.DateTime,default=datetime.datetime.utcnow())

    def to_dict(self):
        data= {c.name:getattr(self,c.name) for c in self.__table__.columns}
        if 'created_on' in data and isinstance(data['created_on'],datetime.datetime):
            data['created_on']=data['created_on'].isoformat()
            data.pop('password','None')
        return data

    def generate_hash(self):
        self.password=generate_password_hash(password=self.password)


    def verify_pass(self,pwd):
        return check_password_hash(self.password,pwd)





