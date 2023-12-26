
from flask import request
from uuid import uuid4
from flask.views import MethodView

from . import bp
from db import cars

from schemas import CarSchema

@bp.route('/cars/<car_id>')
class Car(MethodView):
    @bp.response(200, CarSchema)
    def get(self,car_id):
        try:
            return cars[car_id]  
        except:
            return {'message': 'invalid car'}, 400

@bp.arguments(CarSchema)
def put(self, car_data, car_id):
  try:
    car = cars[car_id]
    car |= car_data
    return { 'message': f'{car["car"]} updated'}, 202
  except KeyError:
    return {'message': "Invalid car"}, 400
      
def delete_car(self, car_id):
  try:
    del cars[car_id]
    return { 'message': f'car Deleted' }, 202
  except:
    return {'message': "Invalid car"}, 400

@bp.route('/cars')
class CarList(MethodView):

  @bp.response(200, CarSchema(many = True))
  def get(self):
   return list(cars.values())
  
  @bp.arguments(CarSchema)
  def post(self, car_data):
    cars[uuid4()] = car_data
    return { 'message' : f'{car_data["car"]} created' }, 201