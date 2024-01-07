from datetime import datetime

from app import db

from werkzeug.security import generate_password_hash, check_password_hash

followers = db.Table( 'followers',
  db.Column('follower_id', db.Integer, db.ForeignKey('cars.id')),
  db.Column('followed_id', db.Integer, db.ForeignKey('cars.id'))  
)

class CarModel(db.Model):

  __tablename__ = 'cars'

  id = db.Column(db.Integer, primary_key = True)
  make = db.Column(db.String(50), nullable = False, unique = True)
  year = db.Column(db.String(75), nullable = False, unique = True)
  followed = db.relationship('CarModel',
                            secondary = 'followers',
                            primaryjoin = followers.c.follower_id == id,
                            secondaryjoin = followers.c.followed_id == id,
                            backref = db.backref('followers', lazy = 'dynamic')
                            )
  # posts = db.relationship(PostModel, backref='author', lazy='dynamic', cascade= 'all, delete')
  
  def __repr__(self):
    return f'<Car: {self.car}>'

  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def from_dict(self, car_dict):
    for k, v in car_dict.items():
      if k != 'password':
        setattr(self, k, v)
      else:
        setattr(self, 'password_hash', generate_password_hash(v))


class ModModel(db.Model):

  __tablename__ = 'mods'

  id = db.Column(db.Integer, primary_key = True)
  tint = db.Column(db.String, nullable = False)
  timestamp = db.Column(db.DateTime, default = datetime.utcnow)
  car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable = False)

  def __repr__(self):
    return f'<Mod: {self.body}>'
  
  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()