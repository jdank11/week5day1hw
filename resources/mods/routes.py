from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from schemas import ModSchema, ModsSchemaNested
from models import ModModel
from . import bp



@bp.route('/<mod_id>')
class Mod(MethodView):

  @bp.response(200, ModsSchemaNested)
  def get(self, mod_id):
    mods = ModModel.query.get(mod_id)
    if mods:
      print(mods.author)
      return mods
    abort(400, message='Invalid mods')

  @bp.arguments(ModSchema)
  def put(self, mod_data ,mod_id):
    mods = ModModel.query.get(mod_id)
    if mods:
      mods.body = mod_data['body']
      mods.commit()   
      return {'message': 'mods updated'}, 201
    return {'message': "Invalid mods id"}, 400

  def delete(self, mod_id):
    mods = ModModel.query.get(mod_id)
    if mods:
      mods.delete()
      return {"message": "mod Deleted"}, 202
    return {'message':"Invalid mod"}, 400

@bp.route('/')
class ModList(MethodView):

  @bp.response(200, ModSchema(many = True))
  def get(self):
    return  list(mods.values())
  
  @bp.arguments(ModSchema)
  def post(self, mod_data):
    try:
      mods = ModModel()
      mods.user_id = mod_data['car_id']
      mods.body = mod_data['body']
      mods.commit()
      return { 'message': "Post Created" }, 201
    except:
      return { 'message': "Invalid car"}, 401