from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from Config import Config


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from models.carmodel import CarModel
from models import ModModel, CarModel

from resources.cars import bp as car_bp
api.register_blueprint(car_bp)

from resources.mods import bp as mod_bp
api.register_blueprint(mod_bp)


