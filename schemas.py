from marshmallow import Schema, fields

class CarSchema(Schema):
  id = fields.Str(dump_only = True)
  make = fields.Str(required = True)
  year = fields.Str(required = True)


class ModSchema(Schema):
  id = fields.Str(dump_only = True)
  body = fields.Str(required = True)
  timestamp = fields.DateTime(dump_only = True)
  car_id = fields.Str(required = True)