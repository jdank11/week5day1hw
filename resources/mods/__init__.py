from flask_smorest import Blueprint

bp = Blueprint('mods', __name__, description='Ops on mods', url_prefix='/mods')

from . import routes