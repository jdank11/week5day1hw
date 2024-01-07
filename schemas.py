from marshmallow import Schema, fields

class CarSchema(Schema):
  id = fields.Str(dump_only = True)
  make = fields.Str(required = True)
  year = fields.Str(required = True)

class CarLogin(Schema):
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )

class ModSchema(Schema):
  id = fields.Str(dump_only = True)
  body = fields.Str(required = True)
  timestamp = fields.DateTime(dump_only = True)
  car_id = fields.Str(required = True)

class ModsSchemaNested(ModSchema):
  cars = fields.Nested(CarSchema, dump_only = True)

class CarsSchemaNested(CarSchema):
 mods = fields.List(fields.Nested(ModSchema), dump_only=True)