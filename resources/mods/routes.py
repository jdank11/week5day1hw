from flask import request
from uuid import uuid4
from flask.views import MethodView

from schemas import ModSchema
from db import *
from . import bp



@bp.route('/<mod_id>')
class Mod(MethodView):

  @bp.response(200, ModSchema)
  def get(self, mod_id):
    try:
      return mods[mod_id]
    except KeyError:
      return {'message': "Invalid mods"}, 400

  @bp.arguments(ModSchema)
  def put(self, mod_data ,mod_id):
    try:
      mod = mods[mod_id]
      if mod_data['user_id'] == mod['user_id']:
        mod['body'] = mod_data['body']
        return { 'message': 'mod Updated' }, 202
      return {'message': "Unauthorized"}, 401
    except:
      return {'message': "Invalid mod Id"}, 400

  def delete(self, mod_id):
    try:
      del mods[mod_id]
      return {"message": "mod Deleted"}, 202
    except:
      return {'message':"Invalid mod"}, 400

@bp.route('/')
class ModList(MethodView):

  @bp.response(200, ModSchema(many = True))
  def get(self):
    return  list(mods.values())
  
  @bp.arguments(ModSchema)
  def post(self, mod_data):
    car_id = mod_data['car_id']
    if car_id in mods:
      mods[uuid4()] = mod_data
      return { 'message': "mod Created" }, 201
    return { 'message': "Invalid car"}, 401