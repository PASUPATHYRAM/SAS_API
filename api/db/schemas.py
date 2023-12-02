from marshmallow import Schema,fields

class Schemas(Schema):
    id=fields.Int(dump_only=True)
    username=fields.Str()
    email=fields.Str()
    phone=fields.Int()
    password=fields.Str(load_only=True)
    role=fields.Str()
    created_on=fields.Str()

