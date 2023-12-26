from flask import Flask
from flask_smorest import Api
from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

from resources.cars import bp as car_bp
api.register_blueprint(car_bp)

from resources.mods import bp as mod_bp
api.register_blueprint(mod_bp)


