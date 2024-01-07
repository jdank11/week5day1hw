from flask_jwt_extended import create_access_token

from models import CarModel

from . import bp 
from schemas import CarLogin

@bp.post('/login')
@bp.arguments(CarLogin)
def login(car_data):
  cars = CarModel.query.filter_by(username = car_data['username']).first()
  if cars and cars.check_password(car_data['password']):
    access_token = create_access_token(car.id)
    return {'token': access_token}
  return {'message': 'Invalid car data'}