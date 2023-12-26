from flask import request
from uuid import uuid4

from app import app
from db import *



@app.get('/mods')
def get_mods():
    return { 'mods': list(mods.values())} 

@app.post('/mods')
def create_mods():
    json_body = request.get_json()
    cars[uuid4()] =json_body
    return { 'your mods' : f'{json_body["tint"]} tint'}, 201

@app.put('/mods/<mods_id>')
def update_post(mods_id):
  try:
    mod = mods[mods_id]
    mod_data = request.get_json()
    if mod_data['car_id'] == mod['car_id']:
      mod['body'] = mod_data['body']
      return { 'message': 'Mod Updated' }, 202
    return {'message': "Unauthorized"}, 401
  except:
    return {'message': "Invalid mod"}, 400

@app.delete('/mods/<mods_id>')
def delete_mod(mods_id):
  try:
    del mods[mods_id]
    return {"message": "mod Deleted"}, 202
  except:
    return {'message':"Invalid mod"}, 400