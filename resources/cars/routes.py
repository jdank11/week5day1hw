
from flask import request
from uuid import uuid4

from app import app
from db import cars


@app.route('/cars')
def cars():
    return { 'cars': list(cars.values())} , 200

@app.route('/cars', methods=["POST"])
def create_car():
    car_data = request.get_json()
    for k in ['make', 'year']:
        if k not in car_data:
            return {'message': "Please include make and year"}, 400
    cars[uuid4()] = car_data
    return { 'your car' : f'{car_data["make"] + car_data["year"]} created'}, 201

@app.put('/cars/<car_id>')
def update_car(car_id):
  try:
    car = cars[car_id]
    car_data = request.get_json()
    car |= car_data
    return { 'message': f'{car["car"]} updated'}, 202
  except KeyError:
    return {'message': "Invalid car"}, 400
      
@app.delete('/cars/<car_id>')
def delete_car(car_id):
  try:
    del cars[car_id]
    return { 'message': f'car Deleted' }, 202
  except:
    return {'message': "Invalid car"}, 400
