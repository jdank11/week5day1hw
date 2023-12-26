from flask_smorest import Blueprint

bp = Blueprint('cars', __name__, description="Operations for cars")

from . import routes