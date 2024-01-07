
from flask import request
from flask_smorest import abort
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required

from . import bp

from schemas import CarSchema, CarsSchemaNested
from models.carmodel import CarModel

@bp.route('/cars/<car_id>')
class Car(MethodView):
    
    @bp.response(200, CarsSchemaNested)
    def get(self,car_id):
        cars = CarModel.query.get(car_id)
        if cars:
          print(cars.posts.all())
          return cars
        else:
          abort(400, message='Car not found')

@jwt_required() 
@bp.arguments(CarSchema)
def put(self, car_data, car_id):
  cars = CarModel.query.get(get_jwt_identity())
  if cars and cars.id == car_id:
    cars.from_dict(car_data)
    cars.commit()
    return { 'message': f'{cars.make} updated'}, 202
  abort(400, message='Car not found')

@jwt_required()       
def delete_car(self, car_id):
  cars = CarModel.query.get(get_jwt_identity())
  if cars == car_id:
    cars.delete()
    return { 'message': f'car Deleted' }, 202
  return {'message': "Invalid car"}, 400

@bp.route('/cars')
class CarList(MethodView):

  @bp.response(200, CarSchema(many = True))
  def get(self):
   return CarModel.query.all()
  
  @bp.arguments(CarSchema)
  def post(self, car_data):
    try: 
      cars = CarModel()
      cars.from_dict(car_data)
      cars.commit()
      return { 'message' : f'{car_data["make"]} created' }, 201
    except:
      abort(400, message='make and year Already taken')


@bp.route('/cars/follow/<followed_id>')
class FollowUser(MethodView):

  @jwt_required()
  def post(followed_id):
    followed = CarModel.query.get(followed_id)
    follower =CarModel.query.get(get_jwt_identity())
    if follower and followed:
      follower.follow(followed)
      followed.commit()
      return {'message':'car followed'}
    else:
      return {'message':'invalid car'}, 400
  @jwt_required()  
  def put(self, followed_id):
    followed = CarModel.query.get(followed_id)
    follower = CarModel.query.get(get_jwt_identity())
    if follower and followed:
      follower.unfollow(followed)
      followed.commit()
      return {'message':'car unfollowed'}
    else:
      return {'message':'invalid car'}, 400